from api.request import RequestCreateEmployeeDto
from db.database import DBSession
from db.models import DBEmployee


def create_employee(session: DBSession, employee: RequestCreateEmployeeDto) -> DBEmployee:
    new_employee = DBEmployee(
        first_name=employee.first_name,
        last_name=employee.last_name,
    )

    session.add_model(new_employee)

    return new_employee
