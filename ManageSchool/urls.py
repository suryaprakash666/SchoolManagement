from django.urls import path, include
from rest_framework import routers
from .Views import Staffhomepage, DataTableView, HomepageView, StaffLoginView, StaffRegisterView, StudentRegisterView
from .Views.apiviews import Dataviewset, Staffdataviewset, Studentdataviewset

router = routers.DefaultRouter()
router.register(r'school', Dataviewset)
router.register(r'staff', Staffdataviewset)
router.register(r'student', Studentdataviewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', HomepageView.homepageview, name="Homepage"),
    path('staffview/', Staffhomepage.staffhomeview, name='Staffhome'),
    path('dynamicview/', Staffhomepage.dynamiccontentview, name='Dynamic'),
    path('sendmessage/', Staffhomepage.send_whatsapp_message, name="Sendmessage"),
    path('datatable/', DataTableView.datatableview, name="Datatable"),
    path('stafflogin/',StaffLoginView.staffloginview, name="Stafflogin"),
    path('staffregister/', StaffRegisterView.staffregisterview, name="Staffregisterlink"),
    path('studentregister/', StudentRegisterView.studentregisterview, name="Studentregisterlink")
]
