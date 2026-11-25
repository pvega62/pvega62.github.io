"""Mechanical typo patterns that a dictionary miss: doubled words, missing
spaces, doubled letters, wrong homophones, and common misspellings.

Runs on the probe strings so nav, footer, and attribute text get covered too.
"""
import json
import re
from pathlib import Path

mapping = json.loads(Path('scratch/typo-map.json').read_text(encoding='utf-8'))
lines = Path('scratch/typo-probe.txt').read_text(encoding='utf-8').split('\n')

DOUBLED_WORD = re.compile(r'\b(\w+)\s+\1\b', re.I)
MISSING_SPACE = re.compile(r'[a-z]{2}[.,;:][A-Z][a-z]')
DOUBLE_SPACE = re.compile(r'[A-Za-z]  +[A-Za-z]')
TRIPLE_LETTER = re.compile(r'\b\w*([a-z])\1\1\w*\b', re.I)
SPACE_BEFORE_PUNCT = re.compile(r'\s+[,.;:!?](?:\s|$)')

COMMON = {
    'teh': 'the', 'adn': 'and', 'hte': 'the', 'thier': 'their', 'recieve': 'receive',
    'recieved': 'received', 'seperate': 'separate', 'seperated': 'separated',
    'occured': 'occurred', 'occurence': 'occurrence', 'definately': 'definitely',
    'accomodate': 'accommodate', 'acheive': 'achieve', 'wich': 'which',
    'alot': 'a lot', 'untill': 'until', 'begining': 'beginning',
    'beleive': 'believe', 'calender': 'calendar', 'comitted': 'committed',
    'concensus': 'consensus', 'dependant': 'dependent', 'existance': 'existence',
    'foriegn': 'foreign', 'goverment': 'government', 'independant': 'independent',
    'neccessary': 'necessary', 'occassion': 'occasion', 'persistant': 'persistent',
    'priviledge': 'privilege', 'publically': 'publicly', 'recomend': 'recommend',
    'refered': 'referred', 'relevent': 'relevant', 'resistence': 'resistance',
    'succesful': 'successful', 'sucessful': 'successful', 'tommorow': 'tomorrow',
    'truely': 'truly', 'wierd': 'weird', 'withing': 'within', 'writting': 'writing',
    'managment': 'management', 'enviroment': 'environment', 'paramter': 'parameter',
    'paramters': 'parameters', 'resouce': 'resource', 'resouces': 'resources',
    'documenation': 'documentation', 'documetation': 'documentation',
    'docmentation': 'documentation', 'responsivness': 'responsiveness',
    'accessibilty': 'accessibility', 'compatability': 'compatibility',
    'intergration': 'integration', 'intergrated': 'integrated',
    'implmentation': 'implementation', 'impliment': 'implement',
    'instalation': 'installation', 'configuraiton': 'configuration',
    'workfow': 'workflow', 'workfloww': 'workflow', 'usabilty': 'usability',
    'navigaton': 'navigation', 'protoype': 'prototype', 'wireframe': 'wireframe',
    'wirefarme': 'wireframe', 'onbaording': 'onboarding', 'onbording': 'onboarding',
    'tecnical': 'technical', 'techincal': 'technical', 'techincial': 'technical',
    'bussiness': 'business', 'buisness': 'business', 'proffesional': 'professional',
    'proffessional': 'professional', 'expereince': 'experience',
    'experiance': 'experience', 'knowlege': 'knowledge', 'langauge': 'language',
    'guaruntee': 'guarantee', 'maintainance': 'maintenance',
    'maintenence': 'maintenance', 'perfomance': 'performance',
    'perfromance': 'performance', 'reccomend': 'recommend',
}

HOMOPHONES = {
    'loose': 'lose', 'theyre': "they're", 'youre': "you're", 'its\u2019': "it's",
}

findings = []

for idx, text in enumerate(lines, start=1):
    src = mapping.get(str(idx), {})
    where = f"{src.get('page', '?')}:{src.get('line', '?')} ({src.get('kind', '?')})"
    body = ' '.join(text.split())

    for m in DOUBLED_WORD.finditer(body):
        if m.group(1).lower() in {'that', 'had', 'is', 'no'}:
            findings.append((where, 'doubled word', m.group(0), body[max(0, m.start() - 40):m.end() + 40]))
        else:
            findings.append((where, 'doubled word', m.group(0), body[max(0, m.start() - 40):m.end() + 40]))

    for m in MISSING_SPACE.finditer(body):
        findings.append((where, 'missing space after punctuation', m.group(0), body[max(0, m.start() - 45):m.end() + 45]))

    for m in SPACE_BEFORE_PUNCT.finditer(body):
        findings.append((where, 'space before punctuation', m.group(0), body[max(0, m.start() - 45):m.end() + 45]))

    for m in TRIPLE_LETTER.finditer(body):
        word = m.group(0).lower()
        if word in {'www', 'aaa', 'eee', 'iii', 'ooo', 'uuu'}:
            continue
        findings.append((where, 'triple letter', m.group(0), body[max(0, m.start() - 40):m.end() + 40]))

    for m in re.finditer(r"\b[A-Za-z']+\b", body):
        w = m.group(0).lower().strip("'")
        if w in COMMON:
            findings.append((where, 'common misspelling', m.group(0), f'{m.group(0)} -> {COMMON[w]}'))
        if w in HOMOPHONES:
            findings.append((where, 'homophone risk', m.group(0), body[max(0, m.start() - 55):m.end() + 55]))

if not findings:
    print('no mechanical typo patterns found')
else:
    print(f'{len(findings)} pattern hits\n')
    for where, kind, hit, ctx in findings:
        print(f'{where}\n  [{kind}] {hit!r}\n  ...{ctx}...\n')
