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

import os
import logging
import speedtest

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.audio import wait_while_speaking 
from mycroft.util.log import getLogger

logger = getLogger(__name__)


__author__ = 'luke5sky'

class speedtestSkill(MycroftSkill):

    def __init__(self):
        super(speedtestSkill, self).__init__(name="speedtestSkill")
        
    @intent_handler(IntentBuilder("").require("Run").require("Speedtest").build())
    def handle_speedtest__intent(self, message):
        servers = []
        # If you want to test against a specific server
        # servers = [1234]
        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()
        s.download()
        s.upload()
        s.results.share()
        results_dict = s.results.dict()
        print(results_dict)
        logger.info("Request finished")

    def shutdown(self):
        super(speedtestSkill, self).shutdown()

    def stop(self):
        pass

def create_skill():
    return speedtestSkill()
