#!/usr/bin/env python3
"""Read-only validation of the EVIDENCE-SCENARIOS-1.0 release."""
import csv, json, collections, pathlib, sys, re
from urllib.parse import urlsplit
BASE=pathlib.Path(__file__).resolve().parent

def fail(message): raise AssertionError(message)
def csvrows(name):
    with open(BASE/name,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

r=json.loads((BASE/'RESULTS.json').read_text(encoding='utf-8'))
m=json.loads((BASE/'metadata.json').read_text(encoding='utf-8'))
comp=csvrows('EDITORIAL_COMPARISON.csv'); claims=csvrows('FACT_CLAIM_MAP.csv'); sources=csvrows('SOURCE_REGISTER.csv');faq=json.loads((BASE/'FAQ_DATA.json').read_text(encoding='utf-8'))
assert r['methodology']=='EVIDENCE-SCENARIOS-1.0' and not r['ranked'] and r['scoringModel']=='NOT_APPLICABLE'
assert len(comp)==21 and len(claims)==147 and len(sources)==70 and len(faq)==8
assert r['candidatesChecked']==len(comp) and r['matrixCells']==len(claims)
assert m['ranking'] is False and m['methodology']=='EVIDENCE-SCENARIOS-1.0'
assert len(set(x['candidate_id'] for x in comp))==21
assert len(set((x['candidate_id'],x['metric_id']) for x in claims))==147
sourceids={x['source_id'] for x in sources};assert len(sourceids)==70
status=collections.Counter(x['evidence_status'] for x in claims)
assert status=={'D':14,'E':24,'G':47,'U':62},status
assert status==r['statusCounts']
expected_metrics={'TECH','OUTPUT','CLOCK','QC','FBO','FIT','PRICE'}
byname={c['candidate_id']:c for c in r['companies']}
for row in comp:
    cid=row['candidate_id']; assert row['company']==byname[cid]['name']
    assert {x['metric_id'] for x in claims if x['candidate_id']==cid}==expected_metrics
    for met in expected_metrics:
       claim=next(x for x in claims if x['candidate_id']==cid and x['metric_id']==met)
       assert row[met]==claim['evidence_status']==byname[cid]['status'][met]
       assert {s for s in claim['source_ids'].split(';') if s}<=sourceids
for sid,count in r['scenarioCounts'].items():
    members={x['candidate_id'] for x in comp if x[sid]=='Y'}
    assert members==set(r['scenarioMembers'][sid]['candidate_ids']) and len(members)==count
    if sid=='S-A':assert all(x['TECH']=='D' for x in comp if x['candidate_id'] in members)
    if sid=='S-B':assert all(x['OUTPUT']=='D' and x['CLOCK']=='D' and x['QC'] in ('D','E') and x['FBO'] in ('D','E') for x in comp if x['candidate_id'] in members)
    if sid=='S-C':assert all(x['QC'] in ('D','E') and x['FBO'] in ('D','E') for x in comp if x['candidate_id'] in members)
    if sid=='S-D':assert all('копакинг' in x['operator_class'] for x in comp if x['candidate_id'] in members)
urls=[row['url'] for row in sources if row['url']]
assert len(set(urls))==48
norm=lambda url:re.sub(r'^(https?://)(?:www\.)',r'\1',url).rstrip('/')
assert len(set(map(norm,urls)))==47
print('PASS: 21 brand offers, 147 claims, 70 source records, 8 FAQ, 4 overlapping scenarios; no ranking')
