from typing import Optional
from asgiref.sync import sync_to_async

from .models import Visit, VisitFreeIP, StatisticSettings
from .schemas import VisitGetterSchema
from .utils import location_api
from .telegram import bot


class StatisticsService:

    def is_visit_free_ip(self, ip: str) -> bool:
        try:
            VisitFreeIP.objects.get(ip=ip)
            return True
        except VisitFreeIP.DoesNotExist:
            return False

    def find_visit_by_ip(self, ip: str) -> Optional[Visit]:
        try:
            return Visit.objects.get(ip=ip)
        except Visit.DoesNotExist:
            return None

    def new_visit(self, visit_getter: VisitGetterSchema):
        if self.is_visit_free_ip(visit_getter.ip):
            return None

        if visit := self.find_visit_by_ip(visit_getter.ip):
            visit.increase_visit(1)
            return None

        location = location_api.get_location(visit_getter.ip)
        Visit.objects.create(
            ip=visit_getter.ip,
            city=location['city'],
            region=location['region'],
            country=location['country'],
            referrer=visit_getter.referrer,
            platform=visit_getter.platform,
            user_agent=visit_getter.user_agent,
        )
        bot.send_message('2145918051', 'asdasdasdasdqdq eqw qweqweqw')


@sync_to_async
def create_settings():
    settings = StatisticSettings.objects.first()
    if not settings:
        StatisticSettings.objects.create(site_name='Portfolio')


statistics_service = StatisticsService()