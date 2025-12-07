from flask import Flask, render_template
import random

app = Flask(__name__)

# Survival tips database 💡
SURVIVAL_TIPS = {
    'academic': [
        "📚 Start assignments early (we know you won't, but we have to say it)",
        "🤝 Form study groups (even if they become gaming sessions)",
        "📝 Attend classes (Netflix can wait!)",
        "🎯 Set realistic goals (not 'finish entire syllabus tonight')",
        "☕ Coffee is your friend, but so is sleep!"
    ],
    'social': [
        "🎉 Join clubs and activities",
        "💬 Network with seniors (they know the shortcuts)",
        "🤗 Be kind to everyone (you never know who'll save you in group projects)",
        "🎮 Balance is key: study hard, play harder!",
        "😊 Remember: everyone is faking confidence"
    ],
    'mental': [
        "🧘 Take breaks (burnout is real!)",
        "🌟 Celebrate small wins",
        "💪 It's okay to ask for help",
        "🌈 Your worth isn't defined by grades",
        "🎭 Imposter syndrome? Everyone has it!"
    ]
}

CRISIS_RESPONSES = {
    'exam': "🚨 Emergency Protocol: 1) Don't panic 2) Make a study plan 3) Start NOW 4) Breathe! You've got this! 💪",
    'project': "🔥 Project Crisis: Break it into tiny chunks. Do ONE thing. Then another. Progress > Perfection! 🎯",
    'life': "🌊 Life feels overwhelming? That's normal! Talk to someone. Take a walk. Remember: this too shall pass. 🌈",
    'deadline': "⏰ Deadline approaching? Priority mode activated! Turn off distractions. Focus on must-haves. You can do this! 🚀"
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/advice/<category>')
def advice(category):
    tips = SURVIVAL_TIPS.get(category, ['Category not found! 🤷'])
    tip = random.choice(tips)
    return render_template('advice.html', category=category, tip=tip)

@app.route('/crisis/<crisis_type>')
def crisis(crisis_type):
    response = CRISIS_RESPONSES.get(crisis_type,
                "🤗 Whatever it is, you'll get through it! Take a deep breath. 💙")
    return render_template('crisis.html', crisis_type=crisis_type, response=response)

@app.route('/motivation/<int:desperation_score>')
def motivation(desperation_score):
    if desperation_score < 3:
        message = "🌟 You're absolutely crushing it! Keep that energy! 💪"
        color = "#2ecc71"
        emoji = "🎉"
    elif desperation_score < 7:
        message = "😅 Hanging in there! Remember: progress over perfection! 📈"
        color = "#f39c12"
        emoji = "☕"
    else:
        message = "🆘 EMERGENCY MOTIVATION DEPLOYED! You are stronger than you think. This is temporary. You've got this! 🫂💙"
        color = "#e74c3c"
        emoji = "🚀"

    return render_template('motivation.html',
                         score=desperation_score,
                         message=message,
                         color=color,
                         emoji=emoji)

if __name__ == '__main__':
    app.run(debug=True)