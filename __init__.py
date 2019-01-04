# Copyright 2018 Lukas Gangel
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import speedtest

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

logger = getLogger(__name__)

__author__ = 'luke5sky'

class speedtestSkill(MycroftSkill):

    def __init__(self):
        super(speedtestSkill, self).__init__(name="speedtestSkill")
        
    @intent_handler(IntentBuilder("").require("Run").require("Speedtest").build())
    def handle_speedtest__intent(self, message):
        try:
            self.speak_dialog('running')
            servers = []
            speed = speedtest.Speedtest()
            speed.get_servers(servers)
            speed.get_best_server()
            speed.download()
            speed.upload()
            speed.results.share()
            result = speed.results.dict()
            downspeed = ('%.2f' % float((result["download"])/1000000)).replace(".", ",")
            upspeed = ('%.2f' % float((result["upload"])/1000000)).replace(".", ",")
            self.speak_dialog('result', {'DOWN': downspeed,'UP': upspeed})
        except:
            self.speak_dialog("error")
        logger.info("speedtest finished")

    def shutdown(self):
        super(speedtestSkill, self).shutdown()

    def stop(self):
        pass

def create_skill():
    return speedtestSkill()
