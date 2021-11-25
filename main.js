const Discord = require('discord.js');
const client = new Discord.Client();
const fs = require('fs');
const { Stream } = require('stream');

require('dotenv').config();
const token = process.env.TOKEN
var connection;

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.login(token)

client.on('message', async msg => {
    if (msg.content === 'ping') {
        msg.reply('shut the fuck up you dumb bitch');
    }

    else if (msg.content === ".join") {
        if (msg.member.voice.channel) {
            connection = await msg.member.voice.channel.join(); 
        }
        else {
            msg.channel.send("i'm not going in there alone pal");
        }
    }

    else if (msg.content === ".leave") {
        if (msg.member.voice.channel) {
            connection = await msg.member.voice.channel.leave(); 
        }
        else {
            msg.channel.send("you're not in a thing");
        }
    }
});

client.on('guildMemberSpeaking', function(member, speaking) {
    if(speaking.bitfield === 0 || member.user.bot) {
        return;
    }

    const audio = connection.receiver.createStream(member.user, { mode: 'pcm'});

    let bufferArray = [];

    audio.on('data', function(chunk) {
        bufferArray.push(chunk);
    });

    audio.on('end', async = () => {
        const buffer = Buffer.concat(bufferArray);
        const date = new Date();
        fs.writeFile(`./read-audio-python/rawaudio/${member.user.tag}_audio_${date.toISOString().match(/\d+/g, "")}`, buffer, (err) =>{
            if (err) console.log(err);
        });
    });
});