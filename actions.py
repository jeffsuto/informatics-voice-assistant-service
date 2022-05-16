from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.domain import Domain
from rasa_core.trackers import EventVerbosity

import logging
logger = logging.getLogger(__name__)

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import UserUtteranceReverted
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted
from rasa_core.events import FollowupAction
from rasa_core.events import BotUttered
from rasa.core.channels import channel

from action_lib import lecturer
from action_lib import student
from action_lib import exam
from action_lib import registration_schedule
from action_lib import procedure
from action_lib import practicum
from action_lib import trial

class CollegeStudentScheduleByDay(Action):
	def name(self):
		return 'action_student_schedule'

	def run(self, dispatcher, tracker, domain):
		day = next(tracker.get_latest_entity_values("day"), None)
		time = next(tracker.get_latest_entity_values("time"), None)
		nbi = next(tracker.get_latest_entity_values("nbi"), None)

		# nbi = tracker.sender_id
		response = None
		if nbi:
			nbi = nbi.replace(" ", "")
			response = student.schedule(nbi, day, time)
		else:
			response = {
				'text': "masukkan NBI anda untuk informasi jadwal kuliah",
				'data': {
					'prev_message': tracker.latest_message['text']
				},
				'intent': 'ask_student_identity'
			}
		dispatcher.utter_custom_json(response)
		return [AllSlotsReset()]

class LecturerSchedule(Action):
	def name(self):
		return 'action_lecturer_schedule'

	def run(self, dispatcher, tracker, domain):
		lecturer_name = next(tracker.get_latest_entity_values("lecturer"), None)
		day = next(tracker.get_latest_entity_values("day"), None)
		time = next(tracker.get_latest_entity_values("time"), None)
		slot_lecturer = tracker.get_slot('lecturer')

		if slot_lecturer or lecturer_name:
			lecturer_name = slot_lecturer
			response = lecturer.schedule(lecturer_name, day, time)
			dispatcher.utter_custom_json(response)
			return [SlotSet('ask_lecturer_schedule',None)]
		else:
			return [SlotSet('ask_lecturer_schedule',True)]

class LecturerLocation(Action):
	def name(self):
		return 'action_lecturer_location'

	def run(self, dispatcher, tracker, domain):
		lecturer_name = next(tracker.get_latest_entity_values("lecturer"), None)
		slot_lecturer = tracker.get_slot('lecturer')

		if slot_lecturer or lecturer_name:
			lecturer_name = slot_lecturer
			response = lecturer.location(lecturer_name)
			dispatcher.utter_custom_json(response)
			return [SlotSet('ask_lecturer_location',None)]
		else:
			return [SlotSet('ask_lecturer_location',True)]

class Lecturer(Action):
	def name(self):
		return 'action_lecturer'

	def run(self, dispatcher, tracker, domain):
		lecturer_name = next(tracker.get_latest_entity_values("lecturer"), None)
		ask_lecturer_location = tracker.get_slot('ask_lecturer_location')
		ask_lecturer_schedule = tracker.get_slot('ask_lecturer_schedule')
		ask_lecturer_whatsapp_number = tracker.get_slot('ask_lecturer_whatsapp_number')
		
		if ask_lecturer_location:
			response = lecturer.location(lecturer_name)
			dispatcher.utter_custom_json(response)
			return [SlotSet('ask_lecturer_location', None)]

		elif ask_lecturer_whatsapp_number:
			response = lecturer.whatsapp_number(lecturer_name)
			dispatcher.utter_custom_json(response)
			return [SlotSet('ask_lecturer_whatsapp_number', None)]

		elif ask_lecturer_schedule:
			response = lecturer.schedule(lecturer_name)
			dispatcher.utter_custom_json(response)
			return [SlotSet('ask_lecturer_schedule', None)]

		else:
			dispatcher.utter_template('utter_unclear', tracker)
			return[SlotSet('lecturer', None)]

class LecturerWhatsappNumber(Action):
	def name(self):
		return 'action_lecturer_whatsapp_number'

	def run(self, dispatcher, tracker, domain):
		lecturer_name = next(tracker.get_latest_entity_values("lecturer"), None)
		slot_lecturer = tracker.get_slot('lecturer')

		if slot_lecturer or lecturer_name:
			lecturer_name = slot_lecturer
			response = lecturer.whatsapp_number(lecturer_name)
			dispatcher.utter_custom_json(response)
			return [SlotSet('ask_lecturer_whatsapp_number', None)]
		else:
			return [SlotSet('ask_lecturer_whatsapp_number', True)]

class ExamSchedule(Action):
	def name(self):
		return 'action_exam_schedule'

	def run(self, dispatcher, tracker, domain):
		exam_type = next(tracker.get_latest_entity_values("exam"), None)
		nbi = next(tracker.get_latest_entity_values("nbi"), None)
		
		if exam_type:
			# nbi = tracker.sender_id
			response = None
			if nbi:
				nbi = nbi.replace(" ", "")
				response = exam.schedule(nbi, exam_type)
			else:
				response = {
					'text': f"masukkan NBI anda untuk informasi jadwal {exam_type}",
					'data': {
						'prev_message': tracker.latest_message['text']
					},
					'intent': 'ask_student_identity'
				}
			dispatcher.utter_custom_json(response)
			return [AllSlotsReset()]
		else:
			dispatcher.utter_template('utter_unclear', tracker)

class RegistrationSchedule(Action):
	def name(self):
		return 'action_registration_schedule'

	def run(self, dispatcher, tracker, domain):
		registration_type = next(tracker.get_latest_entity_values("type"), None)
		practicum = next(tracker.get_latest_entity_values("practicum"), None)
		nbi = tracker.sender_id

		if registration_type or practicum:
			response = registration_schedule.schedule(registration_type, practicum, nbi)
			dispatcher.utter_custom_json(response)
			return [AllSlotsReset()]
		else:
			dispatcher.utter_template('utter_unclear', tracker)
			return[SlotSet('lecturer', None)]

class Procedure(Action):
	def name(self):
		return 'action_procedure'

	def run(self, dispatcher, tracker, domain):
		procedure_type = next(tracker.get_latest_entity_values("type"), None)

		if procedure_type:
			response = procedure.get(procedure_type)
			dispatcher.utter_custom_json(response)
			return [AllSlotsReset()]
		else:
			dispatcher.utter_template('utter_unclear', tracker)

class PracticumValue(Action):
	def name(self):
		return 'action_practicum_value'

	def run(self, dispatcher, tracker, domain):
		practicum_name = next(tracker.get_latest_entity_values("practicum"), None)
		nbi = next(tracker.get_latest_entity_values("nbi"), None)
		
		# nbi = tracker.sender_id
		response = None
		if nbi:
			nbi = nbi.replace(" ", "")
			response = practicum.value(nbi, practicum_name)
		else:
			response = {
				'text': "masukkan NBI anda untuk informasi nilai praktikum",
				'data': {
					'prev_message': tracker.latest_message['text']
				},
				'intent': 'ask_student_identity'
			}
		
		dispatcher.utter_custom_json(response)
		return [AllSlotsReset()]

class PracticumSchedule(Action):
	def name(self):
		return 'action_practicum_schedule'

	def run(self, dispatcher, tracker, domain):
		practicum_name = next(tracker.get_latest_entity_values("practicum"), None)
		nbi = next(tracker.get_latest_entity_values("nbi"), None)
		
		# nbi = tracker.sender_id
		response = None
		if nbi:
			nbi = nbi.replace(" ", "")
			response = practicum.schedule(nbi, practicum_name)
		else:
			response = {
				'text': "masukkan NBI anda untuk informasi jadwal praktikum",
				'data': {
					'prev_message': tracker.latest_message['text']
				},
				'intent': 'ask_student_identity'
			}

		dispatcher.utter_custom_json(response)
		return [AllSlotsReset()]

class TrialSchedule(Action):
	def name(self):
		return 'action_trial_schedule'

	def run(self, dispatcher, tracker, domain):
		trial_type = next(tracker.get_latest_entity_values("type"), None)
		nbi = next(tracker.get_latest_entity_values("nbi"), None)
		
		# nbi = tracker.sender_id
		response = None
		if nbi:
			nbi = nbi.replace(" ", "")
			response = trial.schedule(nbi, trial_type)
		else:
			response = {
				'text': f"masukkan NBI anda untuk informasi jadwal sidang {trial_type}",
				'data': {
					'prev_message': tracker.latest_message['text']
				},
				'intent': 'ask_student_identity'
			}
			
		dispatcher.utter_custom_json(response)
		return [AllSlotsReset()]

class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]
