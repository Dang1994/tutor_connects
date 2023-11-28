from mycroft import MycroftSkill, intent_handler


class WasabiInspector(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('inspector.wasabi.intent')
    def handle_inspector_wasabi(self, message):
        self.speak_dialog('inspector.wasabi')


def create_skill():
    return WasabiInspector()

