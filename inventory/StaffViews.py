from django import Path
from datetime import datetime

def staff_home(request):
	staff_obj = workers.objects.get(admin = request.user.id)
	production_today = parts.objects.filter(mfd_date=datetime.today)
	