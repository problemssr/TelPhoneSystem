from django.db import models
from django.utils import timezone

"""手机信息表"""


class phone_info(models.Model):
    phone_id = models.BigAutoField(verbose_name='ID', primary_key=True)
    phone_name = models.TextField(verbose_name="设备类型")
    phone_brand = models.CharField(max_length=64, verbose_name="设备品牌")
    phone_serial_number = models.TextField(verbose_name="设备序列号")
    phone_source = models.CharField(max_length=64, verbose_name="设备来源", null=True, blank=True)
    phone_IMEI = models.TextField(verbose_name="设备IMEI号", null=True, blank=True)
    user = models.ForeignKey(verbose_name="用户表", to="borrow_info", to_field="phone", on_delete=models.SET_NULL,
                             null=True, blank=True)

    class Meta:
        db_table = "phone_info"


"""借用表"""


class borrow_info(models.Model):
    people_id = models.BigAutoField(verbose_name='ID', primary_key=True)
    people_name = models.CharField(verbose_name="姓名", max_length=32)
    borrow_time = models.DateTimeField(verbose_name="借出时间", default=timezone.now)
    restore_time = models.DateTimeField(verbose_name="归还时间", null=True, blank=True)
    borrow_usage = models.TextField(verbose_name="借用用途", null=True, blank=True)
    phone = models.IntegerField(verbose_name="设备id", unique=True, null=True, blank=True)

    class Meta:
        db_table = "borrow_info"

    def __str__(self):
        return f'{self.people_name, self.borrow_time.strftime("%Y-%m-%d"), self.restore_time.strftime("%Y-%m-%d"), self.borrow_usage}'


"""手机详细信息表"""


class detail_list(models.Model):
    detail_id = models.BigAutoField(verbose_name="ID", primary_key=True)
    detail_name = models.CharField(verbose_name="设备类型", max_length=100)
    detail_storage = models.CharField(verbose_name="入库", max_length=100)
    detail_storage_id = models.IntegerField(verbose_name="入库序号")
    detail_brand = models.CharField(verbose_name="品牌", max_length=100)
    detail_price = models.TextField(verbose_name="报价", null=True, blank=True)
    detail_buyer = models.TextField(verbose_name="卖家数", null=True, blank=True)
    detail_comment = models.TextField(verbose_name="点评", null=True, blank=True)
    detail_comment_num = models.TextField(verbose_name="点评数", null=True, blank=True)
    detail_exposure_date = models.TextField(verbose_name="曝光日期", null=True, blank=True)
    detail_phone_type = models.TextField(verbose_name="手机类型", null=True, blank=True)
    detail_CVT = models.TextField(verbose_name="运营商定制", null=True, blank=True)
    detail_Touchscreen_type = models.TextField(verbose_name="触摸屏类型", null=True, blank=True)
    detail_screen_size = models.TextField(verbose_name="主屏尺寸", null=True, blank=True)
    detail_screen_material = models.TextField(verbose_name="主屏材质", null=True, blank=True)
    detail_screen_resolution = models.TextField(verbose_name="主屏分辨率", null=True, blank=True)
    detail_screen_pixel = models.TextField(verbose_name="屏幕像素密度", null=True, blank=True)
    detail_narrow_bezel = models.TextField(verbose_name="窄边框", null=True, blank=True)
    detail_screen_of = models.TextField(verbose_name="屏幕占比", null=True, blank=True)
    detail_screen_technology = models.TextField(verbose_name="屏幕技术", null=True, blank=True)
    detail_network_type = models.TextField(verbose_name="网络类型", null=True, blank=True)
    detail_3G_network = models.TextField(verbose_name="3G网络", null=True, blank=True)
    detail_2G_spectrum = models.TextField(verbose_name="支持2G频段", null=True, blank=True)
    detail_3GTDSCDMA = models.TextField(verbose_name="3GTDSCDMA", null=True, blank=True)
    detail_3GWCDMA = models.TextField(verbose_name="3GWCDMA", null=True, blank=True)
    detail_3GCDMA = models.TextField(verbose_name="3GCDMA", null=True, blank=True)
    detail_4G = models.TextField(verbose_name="4G", null=True, blank=True)
    detail_WLAN_function = models.TextField(verbose_name="WLAN功能", null=True, blank=True)
    detail_nav = models.TextField(verbose_name="导航", null=True, blank=True)
    detail_connection_sharing = models.TextField(verbose_name="连接与共享", null=True, blank=True)
    detail_NFC = models.TextField(verbose_name="NFC", null=True, blank=True)
    detail_Bluetooth40 = models.TextField(verbose_name="蓝牙40", null=True, blank=True)
    detail_OTG = models.TextField(verbose_name="OTG", null=True, blank=True)
    detail_IR = models.TextField(verbose_name="红外遥控", null=True, blank=True)
    detail_MHL = models.TextField(verbose_name="MHL", null=True, blank=True)
    detail_Bluetooth = models.TextField(verbose_name="蓝牙", null=True, blank=True)
    detail_uplink_rate = models.TextField(verbose_name="理论上行速率", null=True, blank=True)
    detail_downlink_rate = models.TextField(verbose_name="理论下行速率", null=True, blank=True)
    detail_HCE = models.TextField(verbose_name="银联云闪付HCE", null=True, blank=True)
    detail_HCE_zone = models.TextField(verbose_name="HCE感应区", null=True, blank=True)
    detail_4G_network = models.TextField(verbose_name="4G网络", null=True, blank=True)
    detail_OS = models.TextField(verbose_name="操作系统", null=True, blank=True)
    detail_Core = models.TextField(verbose_name="核心数", null=True, blank=True)
    detail_CPU_freq = models.TextField(verbose_name="CPU频率", null=True, blank=True)
    detail_RAM = models.TextField(verbose_name="RAM容量", null=True, blank=True)
    detail_ROM = models.TextField(verbose_name="ROM容量", null=True, blank=True)
    detail_SD = models.TextField(verbose_name="存储卡", null=True, blank=True)
    detail_GB = models.TextField(verbose_name="扩展容量", null=True, blank=True)
    detail_Cell = models.TextField(verbose_name="电池类型", null=True, blank=True)
    detail_MAH = models.TextField(verbose_name="电池容量", null=True, blank=True)
    detail_CPU_type = models.TextField(verbose_name="CPU型号", null=True, blank=True)
    detail_GPU_type = models.TextField(verbose_name="GPU型号", null=True, blank=True)
    detail_user_views = models.TextField(verbose_name="用户界面", null=True, blank=True)
    detail_talk_time = models.TextField(verbose_name="理论通话时间", null=True, blank=True)
    detail_stand_time = models.TextField(verbose_name="理论待机时间", null=True, blank=True)
    detail_camera = models.TextField(verbose_name="摄像头", null=True, blank=True)
    detail_camera_type = models.TextField(verbose_name="摄像头类型", null=True, blank=True)
    detail_back_pixel = models.TextField(verbose_name="后置摄像头像素", null=True, blank=True)
    detail_front_pixel = models.TextField(verbose_name="前置摄像头像素", null=True, blank=True)
    detail_CMOS = models.TextField(verbose_name="传感器类型", null=True, blank=True)
    detail_shooting = models.TextField(verbose_name="视频拍摄", null=True, blank=True)
    detail_Photograph = models.TextField(verbose_name="拍照功能", null=True, blank=True)
    detail_flash = models.TextField(verbose_name="闪光灯", null=True, blank=True)
    detail_Aperture = models.TextField(verbose_name="光圈", null=True, blank=True)
    detail_stylist = models.TextField(verbose_name="造型设计", null=True, blank=True)
    detail_Color = models.TextField(verbose_name="机身颜色", null=True, blank=True)
    detail_Mobile_size = models.TextField(verbose_name="手机尺寸", null=True, blank=True)
    detail_Mobile_weight = models.TextField(verbose_name="手机重量", null=True, blank=True)
    detail_Body_Material = models.TextField(verbose_name="机身材质", null=True, blank=True)
    detail_Operation_type = models.TextField(verbose_name="操作类型", null=True, blank=True)
    detail_sensor_type = models.TextField(verbose_name="感应器类型", null=True, blank=True)
    detail_SIM = models.TextField(verbose_name="SIM卡类型", null=True, blank=True)
    detail_fuselage_interface = models.TextField(verbose_name="机身接口", null=True, blank=True)
    detail_fuselage_characteristics = models.TextField(verbose_name="机身特点", null=True, blank=True)
    detail_audio = models.TextField(verbose_name="音频支持", null=True, blank=True)
    detail_video = models.TextField(verbose_name="视频支持", null=True, blank=True)
    detail_picture = models.TextField(verbose_name="图片支持", null=True, blank=True)
    detail_common_function = models.TextField(verbose_name="常用功能", null=True, blank=True)
    detail_business_function = models.TextField(verbose_name="商务功能", null=True, blank=True)
    detail_service_features = models.TextField(verbose_name="服务特色", null=True, blank=True)
    detail_list1 = models.TextField(verbose_name="包装清单1", null=True, blank=True)
    detail_list2 = models.TextField(verbose_name="包装清单2", null=True, blank=True)
    detail_list3 = models.TextField(verbose_name="包装清单3", null=True, blank=True)
    detail_list4 = models.TextField(verbose_name="包装清单4", null=True, blank=True)
    detail_list5 = models.TextField(verbose_name="包装清单5", null=True, blank=True)
    detail_list6 = models.TextField(verbose_name="包装清单6", null=True, blank=True)
    detail_list7 = models.TextField(verbose_name="包装清单7", null=True, blank=True)
    detail_Novero = models.TextField(verbose_name="保修政策", null=True, blank=True)
    detail_quality_time = models.TextField(verbose_name="质保时间", null=True, blank=True)
    detail_quality_remark = models.TextField(verbose_name="质保备注", null=True, blank=True)
    detail_service_tel = models.TextField(verbose_name="客服电话", null=True, blank=True)
    detail_tel_remark = models.TextField(verbose_name="电话备注", null=True, blank=True)
    detail_field90 = models.TextField(verbose_name="字段90", null=True, blank=True)
    detail_ROOT = models.TextField(verbose_name="是否ROOT", null=True, blank=True)
    detail_ROOT_remark = models.TextField(verbose_name="root详细备注", null=True, blank=True)
    detail_Adb = models.TextField(verbose_name="Adb软件安装", null=True, blank=True)
    detail_device_number = models.TextField(verbose_name="设备号", null=True, blank=True)
    detail_MAC_address = models.TextField(verbose_name="MAC地址", null=True, blank=True)
    detail_remark = models.TextField(verbose_name="备注", null=True, blank=True)
    detail_power_specification = models.TextField(verbose_name="电源适配器规格", null=True, blank=True)
    detail_power_manufacturer = models.TextField(verbose_name="电源适配器厂家", null=True, blank=True)
    detail_purchase_date = models.DateTimeField(verbose_name="购买日期", null=True, blank=True)
    detail_Model = models.TextField(verbose_name="Model", null=True, blank=True)
    detail_alias = models.TextField(verbose_name="别名", null=True, blank=True)
    detail_IMEI = models.TextField(verbose_name="IMEI", null=True, blank=True)
    detail_charging = models.TextField(verbose_name="充电口", null=True, blank=True)
    detail_wireless_charging = models.TextField(verbose_name="支持无线充电功能", null=True, blank=True)

    class Meta:
        db_table = "detail_list"


"""管理员"""


class admin(models.Model):
    username = models.CharField(verbose_name="管理员账号", max_length=64)
    password = models.CharField(verbose_name="管理员密码", max_length=64)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Admin"


"""历史记录表"""


class borrow_history(models.Model):
    history_id = models.BigAutoField(verbose_name='ID', primary_key=True)
    history_name = models.TextField(verbose_name="设备类型")
    history_brand = models.CharField(max_length=64, verbose_name="设备品牌")
    history_phone_id = models.IntegerField(verbose_name='设备编号')
    history_source = models.CharField(max_length=64, verbose_name="设备来源", null=True, blank=True)
    history_IMEI = models.TextField(verbose_name="设备IMEI号", null=True, blank=True)
    history_username = models.CharField(verbose_name="姓名", max_length=32)
    history_borrow_time = models.DateTimeField(verbose_name="借出时间", default=timezone.now)
    history_restore_time = models.DateTimeField(verbose_name="归还时间", null=True, blank=True)
    history_usage = models.TextField(verbose_name="借用用途", null=True, blank=True)

    class Meta:
        db_table = "borrow_history"
