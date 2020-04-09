from mycroft import MycroftSkill, intent_file_handler


class Gmusic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gmusic.intent')
    def handle_gmusic(self, message):
        self.speak_dialog('gmusic')


def create_skill():
    return Gmusic()

