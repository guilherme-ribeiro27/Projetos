const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

client.on("ready",()=>{
    console.log(`Logando com o bot ${client.user.tag}`)
})

client.on("message",(msg)=>{
    console.log(`${msg.author.username}: ${msg.content}`)
})  

client.login("ODU5MTYwMDc3NTc5NzE0NTcw.YNopLA.SKyNAoKM9GL2RR8DaG_xe6sm6Sw")