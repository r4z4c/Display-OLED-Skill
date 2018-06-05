
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'usia'

LOGGER = getLogger(__name__)

class ShowOnDisplaySkill(MycroftSkill):

	def __init__(self):
        	super(ShowOnDisplaySkill, self).__init__(name="ShowOnDisplaySkill")
		self.be_friendly = True

	def initialize(self):
		show_on_display_intent = IntentBuilder("ShowDisplayIntent").
            		require("ShowOnDisplay").build()
        	self.register_intent(show_on_display_intent, self.handle_show_on_display_intent)

	def handle_show_on_display_intent(self, message):
        	self.speak_dialog("is.okay")
