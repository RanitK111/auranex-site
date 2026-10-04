#!/usr/bin/env python3
"""Generates every .html page for the Auranex site. Run from the project root:
    python3 tools/build.py
Edit the CONFIG block or page content here, re-run, then commit the generated files."""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from legal import LEGAL, UPDATED

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ---------------- CONFIG ----------------
BRAND = "Auranex"
DOMAIN = "www.kkgmedia.in"
SITE = "https://www.kkgmedia.in"
EMAIL = "kkgmedia1@gmail.com"
INSTAGRAM = "https://instagram.com/auranex.ai"
CALENDLY = "https://calendly.com/kkgmedia1/30min"
FORM_ACTION = "https://formsubmit.co/" + EMAIL
GSC_VERIFY = "3rVmqFx5GMYv2ODLir5eoJMiS3fGNzJC35-rE_UKqWs"  # kept from the old site
TODAY = datetime.date.today().isoformat()
# ----------------------------------------

INDUSTRIES = {
 "hvac": dict(name="HVAC", icon="❄️", title="AI Receptionist for HVAC Companies",
  tag="Every no-heat and no-cooling call answered, sorted and booked.",
  pain="HVAC calls arrive while your techs are on roofs, in attics and on other jobs. A caller with a broken AC in July calls the next company on the list if nobody picks up.",
  does=["Answers every call, including nights, weekends and peak-season rushes","Collects name, address, system type and the problem","Flags no-heat / no-cooling emergencies and texts your on-call tech or owner","Books estimates, repairs and seasonal tune-ups into your calendar","Answers questions about service areas, hours, financing and maintenance plans","Sends a text summary of every call"],
  calls=[("“My furnace stopped working and it's freezing.”","Gets the address and details, marks it urgent, and alerts your on-call tech right away."),("“Do you do duct cleaning in my area?”","Checks your service area and services, then offers a time for an estimate.")],
  faq=[("Can it dispatch a technician?","It can notify your on-call person immediately by text or call and book the visit into your calendar. Dispatching in your field-service software depends on your tools; tell us what you use."),("What about gas smells or carbon monoxide?","We configure the AI to tell callers to leave the building and call 911 or the gas utility, then alert your team. Emergency safety wording is agreed with you during setup.")]),
 "plumbing": dict(name="Plumbing", icon="🔧", title="AI Receptionist for Plumbers",
  tag="Burst pipes don't wait for office hours. Neither should your phone.",
  pain="Plumbing customers call in a panic, usually when you're under a sink or off-shift. If they get voicemail, they keep dialing until someone answers.",
  does=["Picks up instantly, day or night","Captures the issue, address, access details and urgency","Separates emergencies (leaks, backups, no water) from routine jobs","Books estimates and jobs, or notifies your on-call plumber","Answers questions on service areas, call-out fees and hours","Texts you a clean summary of every call"],
  calls=[("“There's water coming through my ceiling.”","Tells the caller to shut off the main if they can, gathers details, flags it urgent and alerts your on-call plumber."),("“How much to replace a water heater?”","Explains how you quote, then books an on-site estimate.")],
  faq=[("Will it quote prices?","Only what you approve, such as a call-out fee or 'free estimates'. For anything else it books an estimate instead of guessing."),("Does it work with my existing number?","Yes. Calls forward to Auranex, and you keep your current business number.")]),
 "dental": dict(name="Dental", icon="🦷", title="AI Receptionist for Dental Practices",
  tag="Keep the chair full while your team stays with the patient.",
  pain="Front desks are pulled between check-in, insurance questions and the phone. Calls at lunch, after hours and during busy mornings go to voicemail, and new-patient calls are the ones most likely to go elsewhere.",
  does=["Answers every call, including lunch hours and after hours","Books new-patient and returning-patient appointments from your open slots","Handles reschedules, cancellations and reminder confirmations","Answers FAQs: location, hours, accepted insurance list you provide, new-patient steps","Takes messages and routes urgent calls to your on-call process","Fills cancelled slots faster by offering them to callers"],
  calls=[("“I'd like to book a cleaning for next week.”","Offers available times, confirms details and books the visit."),("“I have a toothache and need to be seen.”","Follows your urgent-care script, offers the earliest slot or alerts staff, and says to call 911 for severe swelling or trouble breathing.")],
  faq=[("Is it HIPAA compliant?","We do not claim HIPAA compliance, and we are not a business associate unless we sign a written agreement. The AI is set up to collect scheduling details only. If your practice needs a BAA, tell us before onboarding. See our <a href=\"security.html\">Security page</a>."),("Does it give clinical advice?","No. It never diagnoses or advises on treatment. Clinical questions are passed to your team.")]),
 "roofing": dict(name="Roofing", icon="🏠", title="AI Receptionist for Roofing Contractors",
  tag="After the storm, the first company to answer wins the job.",
  pain="Roofers are on ladders all day, and storm season sends call volume through the roof. Homeowners comparing quotes rarely leave a voicemail; they call the next name on the list.",
  does=["Answers every call, including storm surges and weekends","Captures the address, roof type, damage and insurance-claim status","Books free inspections and estimates in your calendar","Flags active leaks for same-day attention","Answers questions about materials, warranties, financing and service areas","Texts you lead details immediately"],
  calls=[("“A tree hit my roof last night and it's leaking.”","Collects the details, flags it urgent, and alerts your team for same-day response."),("“I need a quote for a full replacement.”","Gets the address and roof details and books an inspection.")],
  faq=[("Can it handle insurance-claim questions?","It collects basic information such as whether a claim has been filed and the carrier, and passes it to your team. It does not give claim advice."),("What happens during a storm rush with many calls at once?","The AI can take many calls at the same time, so callers do not get busy signals.")]),
 "medspa": dict(name="Medspa", icon="✨", title="AI Receptionist for Medspas",
  tag="Treatments take both hands. Let Auranex take the phone.",
  pain="Medspa staff are in treatment rooms most of the day. Prospects who call to book Botox, fillers or laser treatments often move on if no one answers.",
  does=["Answers every call, including evenings and weekends","Books consultations and treatments in your calendar","Answers questions on services, prep and aftercare instructions that you approve","Handles reschedules and cancellations, and sends reminders to reduce no-shows","Sends follow-up texts to callers who did not book (with proper consent)","Gives you a call report so you see missed opportunities"],
  calls=[("“How much is Botox and can I come in Saturday?”","Shares your approved starting price or consultation info, then books a Saturday slot."),("“I had filler yesterday and something feels wrong.”","Does not give medical advice; follows your urgent process, notifies your clinician and tells the caller to seek emergency care if needed.")],
  faq=[("Is it HIPAA compliant?","We do not claim HIPAA compliance, and we are not a business associate unless we sign a written agreement. The AI collects scheduling information, not treatment history. See our <a href=\"security.html\">Security page</a>."),("Will it replace my front desk?","No. It covers calls your team can't take, such as during treatments, after hours and on weekends.")]),
}

NAV = [("index.html","Home"),("industries.html","Industries"),("how-it-works.html","How It Works"),("pricing.html","Pricing"),("contact.html","Contact")]

def head(title, desc, path, extra=""):
    canon = SITE + "/" + ("" if path == "index.html" else path)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="google-site-verification" content="{GSC_VERIFY}">
<link rel="canonical" href="{canon}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,600;0,700;1,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{extra}</head>
<body>
"""

def header(path):
    items = "".join(f'<li><a href="{h}"{" class=\"active\"" if h==path else ""}>{t}</a></li>' for h,t in NAV)
    return f"""<header class="site-header"><div class="wrap nav">
<a class="brand" href="index.html" aria-label="{BRAND} home">AURA<span>NEX</span></a>
<button class="menu-btn" id="menu-btn" aria-label="Menu" aria-expanded="false">☰</button>
<ul id="nav-list">{items}<li><a class="btn btn-gold btn-sm" href="book-demo.html">Book a Demo</a></li></ul>
</div></header>
<main>
"""

def footer():
    ind = "".join(f'<li><a href="{k}.html">{v["name"]}</a></li>' for k,v in INDUSTRIES.items())
    return f"""</main>
<footer class="site-footer"><div class="wrap">
<div class="fgrid">
<div><a class="brand" href="index.html">AURA<span>NEX</span></a>
<p style="margin-top:12px">AI receptionists for US service businesses. Never miss a call or a lead.</p>
<p style="margin-top:12px"><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="{INSTAGRAM}" rel="noopener" target="_blank">Instagram @auranex.ai</a></p></div>
<div><h4>Industries</h4><ul>{ind}</ul></div>
<div><h4>Company</h4><ul><li><a href="how-it-works.html">How It Works</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="contact.html">Contact</a></li><li><a href="book-demo.html">Book a Demo</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="privacy-policy.html">Privacy Policy</a></li><li><a href="terms.html">Terms of Service</a></li><li><a href="cookie-policy.html">Cookie Policy</a></li><li><a href="refund-policy.html">Refund Policy</a></li><li><a href="acceptable-use.html">Acceptable Use</a></li><li><a href="sms-terms.html">SMS Terms</a></li><li><a href="security.html">Security</a></li><li><a href="disclaimer.html">Disclaimer</a></li></ul></div>
</div>
<div class="copy"><span>© {datetime.date.today().year} {BRAND} — A KKG Media company</span><span>Auranex is not an emergency service.</span></div>
</div></footer>
<div id="cookie" role="dialog" aria-live="polite">We use minimal browser storage and Google Fonts to run this site. Details in our <a href="cookie-policy.html">Cookie Policy</a>.
<div class="row"><button class="btn btn-gold btn-sm" data-ok>Got it</button></div></div>
<script src="assets/js/main.js"></script>
</body></html>
"""

def write(path, html):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(html)

def page(path, title, desc, body, extra=""):
    write(path, head(title, desc, path, extra) + header(path) + body + footer())

def faq_html(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items)

CTA = """<section class="alt center"><div class="wrap"><h2>See it answer a real call <span class="gold">in 60 seconds</span></h2>
<p class="lead">Book a free demo and we'll show you how Auranex would work for your business. No commitment, no tech setup on your end.</p>
<p style="margin-top:28px"><a class="btn btn-gold" href="book-demo.html">Book Your Free Demo →</a></p>
<p style="margin-top:14px;color:var(--muted);font-size:.9rem">14-day free trial · No credit card required · Setup in about 48 hours</p></div></section>"""

# ---------- HOME ----------
def home():
    cards = "".join(f'<a class="card" href="{k}.html"><div class="ico">{v["icon"]}</div><h3>{v["name"]}</h3><p>{v["tag"]}</p><span class="more">Learn more →</span></a>' for k,v in INDUSTRIES.items())
    feats = [("📞","Answers every call","Picks up on the first ring, 24/7, including holidays and busy periods."),
             ("📅","Books appointments","Connects to your calendar and books real time slots."),
             ("💬","Answers questions","Services, hours, service areas and policies, answered from information you approve."),
             ("🚨","Flags urgent calls","Spots emergencies and alerts your on-call person right away."),
             ("🔔","Reminders & follow-ups","Text reminders and follow-ups that cut no-shows and recover lost leads."),
             ("📊","Call reports","See every call, booking and missed opportunity in one summary.")]
    fc = "".join(f'<div class="card"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in feats)
    body = f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">AI Receptionists for US Businesses</span>
<h1>Never miss <em class="gold">a call or a lead</em> again.</h1>
<p class="lead">Auranex answers your calls, books appointments and handles customer questions around the clock, built for HVAC, plumbing, dental, roofing and medspa businesses.</p>
<div class="cta"><a class="btn btn-gold" href="book-demo.html">Book a Free Demo</a><a class="btn btn-ghost" href="how-it-works.html">See How It Works</a></div>
<ul class="ticks"><li>Answers every call, day or night</li><li>Books appointments automatically</li><li>Live in about 48 hours</li><li>Built for US service businesses</li></ul>
</div></section>

<section><div class="wrap center"><h2>Built for the businesses <span class="gold">where every call counts</span></h2>
<p class="lead">If a missed call can become a lost job or a lost patient, Auranex is built for you.</p>
<div class="grid g5">{cards}</div></div></section>

<section class="alt"><div class="wrap"><span class="eyebrow">The problem</span><h2>Missed calls are <span class="gold">missed revenue</span></h2>
<p class="lead">You can't answer the phone while you're on a roof, under a sink, or with a patient. When nobody picks up, most callers don't leave a voicemail. They call the next business on the list.</p>
<div class="grid g3">
<div class="card"><h3>After hours</h3><p>Emergencies and evening enquiries come when your office is closed.</p></div>
<div class="card"><h3>On the job</h3><p>Your team is busy doing the work that earns the money, not answering the phone.</p></div>
<div class="card"><h3>Peak rushes</h3><p>Storms, heat waves and cold snaps send many calls at once, and a person can only answer one.</p></div></div></div></section>

<section><div class="wrap"><span class="eyebrow">What it does</span><h2>Everything a receptionist does <span class="gold">and more</span></h2>
<div class="grid g3">{fc}</div></div></section>

<section class="alt"><div class="wrap"><span class="eyebrow">How we're different</span><h2>Not a voicemail. <span class="gold">Not a call center.</span></h2>
<div class="table-wrap"><table><thead><tr><th>Capability</th><th>Auranex</th><th>Answering service</th><th>Voicemail</th></tr></thead><tbody>
<tr><td>Available 24/7</td><td>Yes</td><td>Often limited hours</td><td>Yes</td></tr>
<tr><td>Books appointments directly</td><td>Yes</td><td>Sometimes, manually</td><td>No</td></tr>
<tr><td>Knows your services and policies</td><td>Yes, set up for your business</td><td>Generic script</td><td>No</td></tr>
<tr><td>Caller gets an immediate answer</td><td>Yes</td><td>Yes</td><td>No</td></tr>
<tr><td>Flags and alerts on urgent calls</td><td>Yes</td><td>Depends on provider</td><td>No</td></tr>
<tr><td>Setup time</td><td>About 48 hours</td><td>Varies</td><td>Already have it</td></tr>
</tbody></table></div>
<div class="note">🛡️ <strong>Try it free for 14 days.</strong> Full access, no credit card required. See how many calls it answers and appointments it books before you decide to continue.</div></div></section>

<section><div class="wrap"><div class="founder"><div class="avatar">RK</div><div style="flex:1;min-width:260px"><span class="eyebrow">Why I built this</span>
<h2 style="font-size:1.8rem">A real person behind Auranex</h2>
<p class="lead" style="font-size:1.05rem"><strong style="color:var(--text)">Ranit Kumar</strong>, Founder. Service businesses lose bookings simply because nobody can pick up the phone fast enough. I started Auranex so owners can focus on the work while every caller still gets a fast, helpful answer. Auranex began as an AI receptionist for medspas and now serves HVAC, plumbing, dental, roofing and medspa businesses.</p></div></div></div></section>

<section class="alt"><div class="wrap"><h2>Common questions</h2>{faq_html([
("Will this replace my front desk?","No. It catches the calls your team can't take, such as during jobs and treatments, after hours and during rushes. Many customers keep their staff and use Auranex as backup and overflow."),
("Does it sound robotic?","The voice is natural and conversational, and it is set up around your business, tone and services. We also help you add a short disclosure that callers are speaking with an AI, which many US states and good practice recommend."),
("Do I need new phone equipment?","No. Calls forward from your existing business number. No new hardware and no downtime."),
("What if it can't answer something?","It takes a message and notifies your team immediately, or transfers the call to a live person if you enable that."),
("How much does it cost?","Plans start at $297/month with a 14-day free trial. See the <a href=\"pricing.html\">Pricing page</a>."),
])}</div></section>
{CTA}"""
    page("index.html", "Auranex | AI Receptionist for HVAC, Plumbing, Dental, Roofing & Medspa", "Auranex is an AI receptionist for US service businesses. It answers every call, books appointments and handles questions 24/7 for HVAC, plumbing, dental, roofing and medspa.", body)

# ---------- INDUSTRIES ----------
def industries_index():
    cards = "".join(f'<a class="card" href="{k}.html"><div class="ico">{v["icon"]}</div><h3>{v["name"]}</h3><p>{v["tag"]}</p><span class="more">See how it works for {v["name"].lower()} →</span></a>' for k,v in INDUSTRIES.items())
    body = f"""<section class="hero"><div class="wrap"><span class="eyebrow">Industries</span><h1>One AI receptionist, <em class="gold">tuned to your trade.</em></h1>
<p class="lead">Auranex is set up around how your business actually works: your services, your urgency rules, your calendar and your tone.</p></div></section>
<section><div class="wrap"><div class="grid g3">{cards}</div>
<div class="note">Don't see your industry? Other appointment- and call-driven businesses often fit too. <a href="contact.html">Tell us about yours</a>.</div></div></section>{CTA}"""
    page("industries.html", "Industries | Auranex AI Receptionist", "Auranex AI receptionists for HVAC, plumbing, dental, roofing and medspa businesses.", body)

def industry_page(key, v):
    others = "".join(f'<a class="btn btn-ghost btn-sm" href="{k}.html" style="margin:4px 6px 0 0">{o["name"]}</a>' for k,o in INDUSTRIES.items() if k != key)
    does = "".join(f"<li>{x}</li>" for x in v["does"])
    calls = "".join(f'<div class="card"><h3 style="font-size:1.05rem">{q}</h3><p>{a}</p></div>' for q,a in v["calls"])
    body = f"""<section class="hero"><div class="wrap"><span class="eyebrow">{v['icon']} {v['name']}</span><h1>{v['title'].replace('AI Receptionist for ','AI Receptionist for <em class="gold">')}</em></h1>
<p class="lead">{v['tag']}</p>
<div class="cta"><a class="btn btn-gold" href="book-demo.html">Book a Free Demo</a><a class="btn btn-ghost" href="pricing.html">See Pricing</a></div></div></section>
<section><div class="wrap"><div class="grid g2" style="align-items:start"><div><h2>The problem</h2><p class="lead">{v['pain']}</p></div>
<div><h2>What Auranex does</h2><ul class="check">{does}</ul></div></div></div></section>
<section class="alt"><div class="wrap"><h2>Example calls</h2><p class="lead">Illustrative scenarios of how a call can be handled. Exact behaviour is set up with you.</p><div class="grid g2">{calls}</div></div></section>
<section><div class="wrap"><h2>{v['name']} questions</h2>{faq_html(v['faq'])}
<p style="margin-top:34px;color:var(--muted)">Other industries:</p><div>{others}</div></div></section>{CTA}"""
    page(f"{key}.html", f"{v['title']} | Auranex", f"{v['tag']} Auranex answers calls, books appointments and handles questions 24/7 for {v['name'].lower()} businesses.", body)

# ---------- HOW IT WORKS ----------
def how():
    body = f"""<section class="hero"><div class="wrap"><span class="eyebrow">How it works</span><h1>Live in about 48 hours, <em class="gold">zero disruption.</em></h1>
<p class="lead">We handle the setup. You just take more bookings.</p></div></section>
<section><div class="wrap steps">
<div class="step"><h3>We learn your business</h3><p>A quick 30-minute call to collect your services, pricing rules, hours, service area, FAQs, urgency rules and booking process.</p></div>
<div class="step"><h3>We build your AI receptionist</h3><p>We configure a voice agent with your business name, tone and approved answers, and connect your calendar and alerts.</p></div>
<div class="step"><h3>We connect it to your phone</h3><p>Your existing number forwards to Auranex. No new equipment and no technical skills needed.</p></div>
<div class="step"><h3>You stop missing calls</h3><p>Calls are answered, appointments booked and urgent issues flagged, while you get a summary of every call.</p></div></div></section>
<section class="alt"><div class="wrap"><h2>What's included</h2><div class="grid g3">
<div class="card"><div class="ico">📞</div><h3>Call answering</h3><p>24/7, including holidays.</p></div>
<div class="card"><div class="ico">📅</div><h3>Booking</h3><p>Real-time appointments in your calendar.</p></div>
<div class="card"><div class="ico">🚨</div><h3>Urgent alerts</h3><p>Emergencies flagged to your on-call person.</p></div>
<div class="card"><div class="ico">🔔</div><h3>Reminders</h3><p>Texts that reduce no-shows (Growth and Pro).</p></div>
<div class="card"><div class="ico">🔄</div><h3>Reschedules</h3><p>Callers can move or cancel without staff time.</p></div>
<div class="card"><div class="ico">📊</div><h3>Reports</h3><p>Monthly, or weekly on Pro.</p></div></div></div></section>
<section><div class="wrap"><h2>Questions</h2>{faq_html([
("Does it sound robotic?","The voice is natural and conversational. We recommend a short greeting that tells callers they are speaking with an AI assistant."),
("How does it know my services and pricing?","During onboarding we build a knowledge base from the information you provide. The AI answers only from that and takes a message when it doesn't know."),
("Can it book into my calendar system?","It connects to common calendar and booking tools. Tell us which you use and we'll confirm compatibility before you commit."),
("What happens to caller information?","It is stored securely and used only to run your service. Recordings and transcripts are deleted after 90 days by default. See our <a href=\"privacy-policy.html\">Privacy Policy</a>."),
("What about urgent or emergency calls?","You decide the rules. The AI flags urgent calls and alerts your team, and tells callers to dial 911 for real emergencies. It is not an emergency service."),
])}</div></section>{CTA}"""
    page("how-it-works.html", "How It Works | Auranex AI Receptionist", "See how Auranex sets up and runs your AI receptionist and goes live in about 48 hours.", body)

# ---------- PRICING ----------
def pricing():
    def plan(name, price, blurb, feats, pop=False):
        li = "".join(f"<li>{f}</li>" for f in feats)
        return f'<div class="card price{" pop" if pop else ""}">{"<span class=badge>Most popular</span>" if pop else ""}<h3>{name}</h3><div class="amt">{price}<small>/mo</small></div><p>{blurb}</p><ul class="check">{li}</ul><a class="btn {"btn-gold" if pop else "btn-ghost"}" href="book-demo.html">Start Free Trial</a></div>'
    plans = plan("Starter","$297","For owner-operators and small teams.",["Up to 200 calls/month","24/7 call answering","Appointment booking","FAQ handling","Monthly call report"]) + \
            plan("Growth","$497","For established businesses ready to scale.",["Unlimited calls","24/7 call answering","Booking + reminders","Reschedule and cancellation handling","SMS follow-ups","Priority support"], True) + \
            plan("Pro","$797","For multi-location and high-volume businesses.",["Everything in Growth","Multiple locations","Custom AI voice and persona","CRM integration","Dedicated account manager","Weekly performance reports"])
    body = f"""<section class="hero"><div class="wrap center"><span class="eyebrow">Pricing</span><h1>Less than one <em class="gold">missed job.</em></h1>
<p class="lead">Simple monthly pricing in US dollars. Setup and onboarding are included. No long-term contracts.</p></div></section>
<section><div class="wrap"><div class="grid g3">{plans}</div>
<div class="note">🛡️ <strong>14-day free trial.</strong> Full access, no credit card required. Cancel anytime. Fair-use and plan limits apply as described in our <a href="terms.html">Terms</a>.</div></div></section>
<section class="alt"><div class="wrap"><h2>Before you commit</h2>{faq_html([
("Is there a setup fee?","No. Setup, onboarding and training the AI on your business are included in every plan."),
("Can I cancel anytime?","Yes. Plans are month-to-month. See our <a href=\"refund-policy.html\">Refund &amp; Cancellation Policy</a>."),
("What happens during the free trial?","You get full access for 14 days so you can see real calls answered before paying."),
("How does billing work?","Plans bill monthly from the day your trial ends. You can upgrade, downgrade or cancel at any time."),
("Do you charge per industry?","No. The same plans apply to HVAC, plumbing, dental, roofing and medspa businesses."),
])}</div></section>{CTA}"""
    page("pricing.html", "Pricing | Auranex AI Receptionist", "Auranex plans from $297/month with a 14-day free trial. Setup included, no long-term contracts.", body)

# ---------- CONTACT ----------
def contact():
    opts = "".join(f"<option>{v['name']}</option>" for v in INDUSTRIES.values()) + "<option>Other</option>"
    body = f"""<section class="hero"><div class="wrap"><span class="eyebrow">Contact</span><h1>Let's talk about <em class="gold">your business.</em></h1>
<p class="lead">Send a message, email us directly, or book a free 30-minute demo.</p></div></section>
<section><div class="wrap"><div class="grid g3" style="margin-top:0">
<a class="card" href="mailto:{EMAIL}"><div class="ico">✉️</div><h3>Email</h3><p>{EMAIL}</p></a>
<a class="card" href="{INSTAGRAM}" target="_blank" rel="noopener"><div class="ico">📷</div><h3>Instagram</h3><p>@auranex.ai</p></a>
<a class="card" href="book-demo.html"><div class="ico">📅</div><h3>Book a call</h3><p>Free 30-minute demo</p></a></div>
<h2 style="margin-top:56px">Send us a message</h2>
<form action="{FORM_ACTION}" method="POST">
<input type="hidden" name="_subject" value="New Auranex website enquiry">
<input type="hidden" name="_next" value="{SITE}/thanks.html">
<input type="hidden" name="_captcha" value="true">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<div><label for="n">Your name</label><input id="n" name="name" required autocomplete="name"></div>
<div><label for="b">Business name</label><input id="b" name="business" required autocomplete="organization"></div>
<div><label for="e">Email</label><input id="e" type="email" name="email" required autocomplete="email"></div>
<div><label for="p">Phone (optional)</label><input id="p" type="tel" name="phone" autocomplete="tel"></div>
<div><label for="i">Industry</label><select id="i" name="industry">{opts}</select></div>
<div><label for="m">How can we help?</label><textarea id="m" name="message" required></textarea></div>
<label class="check-row"><input type="checkbox" required> <span>I agree to be contacted about my enquiry and have read the <a href="privacy-policy.html">Privacy Policy</a>.</span></label>
<button class="btn btn-gold" type="submit">Send message</button>
</form></div></section>"""
    page("contact.html", "Contact | Auranex AI Receptionist", "Contact Auranex by email, Instagram or form, or book a free 30-minute demo.", body)

def book():
    body = f"""<section class="hero"><div class="wrap"><span class="eyebrow">Free 30-minute demo</span><h1>See it answer a real call <em class="gold">in 60 seconds.</em></h1>
<p class="lead">Pick a time. No commitment and no tech setup on your end, just a walkthrough of how Auranex would work for your business.</p>
<p style="margin-top:28px"><button class="btn btn-gold" id="load-cal" type="button">Show booking calendar</button>
<a class="btn btn-ghost" href="{CALENDLY}" target="_blank" rel="noopener">Open booking page directly →</a></p>
<p style="margin-top:12px;color:var(--muted);font-size:.88rem">Scheduling is provided by Calendly, which is only loaded when you click the button. See our <a href="cookie-policy.html">Cookie Policy</a>.</p>
<div class="calendly" id="cal-holder" style="background:transparent;border:0"></div></div></section>"""
    page("book-demo.html", "Book a Demo | Auranex AI Receptionist", "Book a free 30-minute demo to see how Auranex would work for your business.", body)

def thanks():
    body = f"""<section class="hero"><div class="wrap center" style="min-height:40vh"><span class="eyebrow">Message sent</span><h1>Thank you, <em class="gold">we'll be in touch.</em></h1>
<p class="lead" style="margin:20px auto 30px">We usually reply within one business day. Want to skip the wait?</p>
<a class="btn btn-gold" href="book-demo.html">Book a demo</a></div></section>"""
    page("thanks.html", "Thank you | Auranex", "Thanks for contacting Auranex.", body, '<meta name="robots" content="noindex">\n')

def notfound():
    body = """<section class="hero"><div class="wrap center" style="min-height:45vh"><span class="eyebrow">404</span><h1>Page <em class="gold">not found.</em></h1>
<p class="lead" style="margin:20px auto 30px">That page doesn't exist or has moved.</p><a class="btn btn-gold" href="/">Back to home</a></div></section>"""
    # absolute asset paths so 404 works from any URL depth
    html = head("Page not found | Auranex", "Page not found.", "404.html", '<meta name="robots" content="noindex">\n<base href="/">\n') + header("404.html") + body + footer()
    write("404.html", html)

def legal_pages():
    nav = "".join(f'<a href="{k}.html">{v[0]}</a>' for k,v in LEGAL.items())
    for k,(title,html) in LEGAL.items():
        body = f"""<div class="legal"><span class="eyebrow">Legal</span><h1>{title}</h1><p class="upd">Last updated: {UPDATED}</p>
<div class="legal-nav">{nav}</div>{html}</div>"""
        page(f"{k}.html", f"{title} | Auranex", f"{title} for Auranex, operated by KKG Media.", body)

def static_files():
    pages = ["index.html","industries.html"] + [f"{k}.html" for k in INDUSTRIES] + ["how-it-works.html","pricing.html","contact.html","book-demo.html"] + [f"{k}.html" for k in LEGAL]
    urls = "".join(f"<url><loc>{SITE}/{'' if p=='index.html' else p}</loc><lastmod>{TODAY}</lastmod></url>\n" for p in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thanks.html\n\nSitemap: {SITE}/sitemap.xml\n")
    write("CNAME", DOMAIN + "\n")
    write(".nojekyll", "")
    write("assets/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="#1a1305"/><text x="32" y="44" font-family="Georgia,serif" font-size="36" font-weight="700" text-anchor="middle" fill="#d9a441">A</text></svg>\n')

if __name__ == "__main__":
    home(); industries_index()
    for k,v in INDUSTRIES.items(): industry_page(k,v)
    how(); pricing(); contact(); book(); thanks(); notfound(); legal_pages(); static_files()
    print("Built", len([f for f in os.listdir(ROOT) if f.endswith('.html')]), "pages")
