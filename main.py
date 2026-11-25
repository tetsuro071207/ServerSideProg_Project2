from flask import Flask, redirect, render_template, request, url_for
import api_client

app = Flask(__name__)

@app.route("/")
def home():
    skip = request.args.get("skip", default=0, type=int)
    limit = request.args.get("limit", default=100, type=int)
    view_id = request.args.get("view", type=int)
    edit_id = request.args.get("edit", type=int)

    all_ops = api_client.get_operators(skip=skip, limit=limit)
    selected_op = api_client.get_operator(view_id) if view_id else None
    edit_op = api_client.get_operator(edit_id) if edit_id else None

    return render_template(
        "base.html",
        operators=all_ops,
        selected_op=selected_op,
        edit_op=edit_op,
        skip=skip,
        limit=limit,
    )

@app.route("/find")
def find_operator():
    op_id = request.args.get("op_id", type=int)
    if not op_id:
        return redirect(url_for("home"))
    return redirect(url_for("operator_detail", op_id=op_id))


@app.route("/operator/<int:op_id>")
def operator_detail(op_id):
    op = api_client.get_operator(op_id)
    if not op:
        return "Operator not found", 404
    return render_template("operator_detail.html", operator=op)


@app.route("/create", methods=["POST"])
def create_operator():
    payload = {
        "OperatorName": request.form["OperatorName"],
        "Health": int(request.form["Health"]),
        "Speed": int(request.form["Speed"]),
        "Difficulty": int(request.form["Difficulty"]),
        "IsAttacker": "IsAttacker" in request.form,
    }
    api_client.create_operator(payload)
    return redirect(url_for("home"))


@app.route("/update/<int:op_id>", methods=["POST"])
def update_operator(op_id):
    payload = {
        "OperatorName": request.form["OperatorName"],
        "Health": int(request.form["Health"]),
        "Speed": int(request.form["Speed"]),
        "Difficulty": int(request.form["Difficulty"]),
        "IsAttacker": "IsAttacker" in request.form,
    }
    api_client.update_operator(op_id, payload)
    return redirect(url_for("home"))


@app.route("/delete/<int:op_id>", methods=["POST"])
def delete_operator(op_id):
    api_client.delete_operator(op_id)
    return redirect(url_for("home"))
