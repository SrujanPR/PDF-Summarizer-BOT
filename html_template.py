# CSS for chat message styling and theme toggle
css = '''
<style>
/* Base styles for the chat */
.chat-message {
    padding: 1rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
}
.chat-message.user {
    background-color: #FFB74D;  /* Light orange for user */
}
.chat-message.bot {
    background-color: #FF8A65;  /* Deeper orange for bot */
}
.chat-message .avatar {
    width: 10%;
}
.chat-message .avatar img {
    max-width: 50px;
    max-height: 50px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 80%;
    padding: 0 1rem;
    color: #fff;
}
footer {
    visibility: hidden;
}
</style>
'''

# HTML for the bot message template (now applied directly within `app.py`)
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.icons8.com/carbon-copy/100/bot.png" alt="Bot">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.icons8.com/laces/64/user.png" alt="User">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
