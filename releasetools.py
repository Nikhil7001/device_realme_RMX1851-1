# Copyright (C) 2009 The Android Open Source Project
# Copyright (C) 2019 The Mokee Open Source Project
# Copyright (C) 2019 The LineageOS Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import common
import re

def FullOTA_InstallEnd(info):
  OTA_UpdateFirmware(info)
  return

def OTA_UpdateFirmware(info):
  info.script.AppendExtra('ui_print("Flashing firmware images");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/abl.img", "/dev/block/bootdevice/by-name/abl");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl.img", "/dev/block/bootdevice/by-name/xbl");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/xbl_config.img", "/dev/block/bootdevice/by-name/xbl_config");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/dpAP.img", "/dev/block/bootdevice/by-name/apdp");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/dtbo.img", "/dev/block/bootdevice/by-name/dtbo");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/tz.img", "/dev/block/bootdevice/by-name/tz");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/modem.img", "/dev/block/bootdevice/by-name/modem");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/DRIVER.img", "/dev/block/bootdevice/by-name/DRIVER");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/qupv3fw.img", "/dev/block/bootdevice/by-name/qupfw");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/oppo_sec.img", "/dev/block/bootdevice/by-name/oppo_sec");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/splash.img", "/dev/block/bootdevice/by-name/splash");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/devcfg.img", "/dev/block/bootdevice/by-name/devcfg");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/dpMSA.img", "/dev/block/bootdevice/by-name/msadp");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/BTFM.img", "/dev/block/bootdevice/by-name/bluetooth");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/static_nvbk.img", "/dev/block/bootdevice/by-name/oppostanvbk");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/dspso.img", "/dev/block/bootdevice/by-name/dsp");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib.img", "/dev/block/bootdevice/by-name/cmnlib");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/cmnlib64.img", "/dev/block/bootdevice/by-name/cmnlib64");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/aop.img", "/dev/block/bootdevice/by-name/aop");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/storsec.img", "/dev/block/bootdevice/by-name/storsec");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/keymaster64.img", "/dev/block/bootdevice/by-name/keymaster");')
  info.script.AppendExtra('package_extract_file("install/firmware-update/hyp.img", "/dev/block/bootdevice/by-name/hyp");')
  info.script.AppendExtra('block_image_update("/dev/block/bootdevice/by-name/vendor", package_extract_file("install/firmware-update/vendor.transfer.list"), "install/firmware-update/vendor.new.dat.br", "install/firmware-update/vendor.patch.dat") ||')
  info.script.AppendExtra('  abort("E1001: Failed to update system image.");')
