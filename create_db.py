from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db_models.base import Base
from db_models.Operators import DBOperator
from db_models.Weapons import DBWeapons
from db_models.Attachments import DBAttachments
from db_models.Gadgets import DBGadgets
from db_models.Utilities import DBUtilities
from db_models.Maps import DBMaps
from db_models.Defenders import DBDefenders
from db_models.Attackers import DBAttackers
from db_models.OperatorWeapons import DBOperatorWeapons
from db_models.OperatorUtilities import DBOperatorUtilities

from db_models.DBdata import OperatorData, WeaponsData, AttachmentData, GadgetData, UtilityData, MapData, DefenderData, AttackerData, OperatorWeaponData, OperatorUtilityData

from api.database import SQLALCHEMY_DATABASE_URL

all_models = [
    DBOperator,
    DBWeapons,
    DBAttachments,
    DBGadgets,
    DBUtilities,
    DBMaps,
    DBDefenders,
    DBAttackers,
    DBOperatorWeapons,
    DBOperatorUtilities
]

all_data = [
    OperatorData,
    WeaponsData,
    AttachmentData,
    GadgetData,
    UtilityData,
    MapData,
    DefenderData,
    AttackerData,
    OperatorWeaponData,
    OperatorUtilityData
]

def populate(engine):
    with Session(engine) as session:
        for model in all_models:
            session.query(model).delete()

        for tabledata in all_data:
            session.add_all(tabledata)
        
        # Add all of the rest of the tables
        session.commit()


def main():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    populate(engine)
    print("Siege DB file created")


if __name__ == '__main__':
    main()