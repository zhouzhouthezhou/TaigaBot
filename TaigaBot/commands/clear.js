const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
			.setName('clear')
			.setDescription('Deletes messages')
			.setDefaultMemberPermissions(0)
			.addIntegerOption(option => option
				.setName('int')
				.setDescription('Enter an integer')
				.setRequired(true))
			.addUserOption(option => option
				.setName('user')
				.setDescription('Enter a User')),
	async execute(message){
		const Messages = message.channel.messages.fetch();
		const user = message.options.getMember("user")
		
		if (user) {
			const userMessages = (await Messages).filter((m) => m.author.id === user.id);
			await message.channel.bulkDelete(userMessages, true);
			await message.reply({ content: `Messages Deleted From ${user}`, ephemeral: true });
		}
		else{
			message.channel.bulkDelete(message.options.getInteger('int'),true);
			await message.reply({ content: 'Messages Deleted', ephemeral: true });
		}
		
	}
};