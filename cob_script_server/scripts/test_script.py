#!/usr/bin/python

import roslib
roslib.load_manifest('cob_script_server')
import rospy

from simple_script_server import script

class TestScript(script):
		
	def Initialize(self):
		self.sss.init("tray")
		#self.sss.init("torso")
		#self.sss.init("arm")
		#self.sss.init("sdh")
		
	def Run(self): 
		#self.sss.SpeakStr("Hallo","FEST_EN")
		#self.sss.sleep(1)

		# init poses
		handle01 = self.sss.move("arm","folded",False)
		self.sss.move("torso","home",False)
		self.sss.move("sdh","home",False)
		self.sss.move("tray","down")
		handle01.wait()
		self.sss.move("base","home")

		#test
		#self.sss.move("torso",[[0.1,0,0.15,0]])
		#self.sss.move("torso","home")
#		self.sss.moveCartRel("arm", [0.0, 0.0, 0.0], [0.0, 0.0, 90.0/180.0*3.1415926])
#		self.sss.Speak("sentence1","WAV_DE")
#		self.sss.Speak("sentence1","FEST_EN")

		#grasp
		self.sss.move("base","kitchen")
		handle01 = self.sss.move("arm","pregrasp",False)
		self.sss.move("sdh","cylopen")
		handle01.wait()
		self.sss.move("arm","grasp")
		#self.sss.moveCartRel("arm", [-0.2, 0.0, 0.0], [0.0, 0.0, 0.0])
		self.sss.move("sdh","cylclosed")

		#place on tablet
		handle01 = self.sss.move("arm","grasp-to-tablet",False)
		self.sss.move("tray","up",False)
		handle01.wait()
		#print handle01.get_error_code()
		self.sss.move("sdh","cylopen")
		
		#move back to save poses
		handle03 = self.sss.move("arm","tablet-to-folded",False)
		self.sss.sleep(3)
		self.sss.move("sdh","home",False)
		handle03.wait()
		
		#deliver
		self.sss.move("base","order")
		self.sss.move("torso","nod")
		self.sss.wait_for_input()
		self.sss.sleep(3)
		
		#drive back to home
		self.sss.move("tray","down",False)
		self.sss.move("base","home")
		
if __name__ == "__main__":
	SCRIPT = TestScript()
	SCRIPT.Start()
