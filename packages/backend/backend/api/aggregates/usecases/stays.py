from ..services.aggregates import AggregateService


def get_stays(user_id: int):
    service = AggregateService()
    response = service.get_stays_data(user_id)
    return response
