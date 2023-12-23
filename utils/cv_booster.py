from utils.gpt_tools import gpt_request, get_promopt
from utils.pdf_tools import read_file
import json
from readability import Readability

class cvBooster:

    prompts = json.load(open('./test/prompts.json', 'r'))

    def __init__(self, path) -> None:
        self.path = path
        self.text = read_file(path)
        self.infos = ""
        self.education = ""
        self.jobs = ""
        self.skills = ""
        self.other = ""
        self.sections()
        self.flesch_kincaid = ""
        self.readability_matrics()

    def sections(self):
        sections = gpt_request(prompt=1, context=self.text)
        self.infos = sections['infos']
        self.education = sections['education']
        self.jobs = sections['jobs']
        self.skills = sections['skills']
        self.other = sections['other']

    def readability_matrics(self):
        r = Readability(self.text)
        self.flesch_kincaid = r.flesch_kincaid()

    def re_write(self, section, issue, *argv):
        prompt, model, temperature = get_promopt(self.prompts, issue)
        return gpt_request(prompt, section, model, temperature)
    
    def compute_issue(self, priotity=0):
        return "summarize"