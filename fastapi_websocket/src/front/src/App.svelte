<script lang="ts">
	import { v4 as uuidv4 } from "uuid";
	import MultipleTextInput from "./components/MultipleTextInput.svelte";
	let text = "";
	let editable = true;

	let clientId = uuidv4();
	let currentId = uuidv4();
	let items = [];

	var ws = new WebSocket(`ws://localhost:8000/ws/${clientId}`);
	ws.onmessage = function (event) {
		const record = JSON.parse(event.data);
		if (items.find((element) => element.message_id == record.message_id) === undefined) {
			console.log(record);
			items = [...items, record];
		}
	};

	function handleKeyPress(e) {
		let event = e.detail.event;
		if (event.code === "Enter" && event.ctrlKey) {
			text = e.detail.text;
			editable = false;
			const record = { client_id: clientId, message_id: currentId, message: text };
			ws.send(JSON.stringify(record));

			currentId = uuidv4();
			text = "";
		}
	}

	function handleClick(e) {
		editable = true;
	}
</script>

<main>
	{#each items as item (item.message_id)}
		<div class="record">
			<div class="header">{item.receive_timestamp}</div>
			<MultipleTextInput
				text={item.message}
				{editable}
				fill={true}
				on:keypress={handleKeyPress}
				on:click={handleClick}
			/>
		</div>
	{/each}
	<div class="record">
		<MultipleTextInput
			{text}
			{editable}
			fill={true}
			on:keypress={handleKeyPress}
			on:click={handleClick}
		/>
	</div>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	.record {
		margin: 16px;
		width: 480px;
	}
	.header {
		font-size: 12px;
		text-align: left;
		margin: 0;
	}
</style>
