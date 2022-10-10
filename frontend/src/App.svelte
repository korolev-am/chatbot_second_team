<script lang="ts">
  import { onMount } from "svelte";

  // store subscriptions
  type Message = {
    author: "bot" | "user";
    data: string;
  };
  type ButtonMsg = {
    name: string;
    text: string;
  };


  let messages: Message[] = [];
  let userMessage: string;
  let buttons: ButtonMsg[] = [];
  let is_buttons: number = 1;
  let id: string;

  let socket: WebSocket;

  onMount(() => {
    socket = new WebSocket("ws://localhost:9191/chat");
    socket.onmessage = (message) => {
      id = message.data.id;
      buttons = message.data.buttons;
      is_buttons = message.data.is_buttons;
      messages = [
        ...messages,
        {
          author: "bot",
          data: message.data.text,
        },
      ];
    };
    socket.addEventListener("open", () => {
      console.log("Opened");
    });
  });

  const sendHandler = async () => {
    socket.send(id + ";" + userMessage);
    messages = [
      ...messages,
      {
        author: "user",
        data: userMessage,
      },
    ];
    userMessage = "";
  };

  const questionHandler = (value: string) => {
    // if STR
    socket.send(id + ";" + value);
    messages = [
      ...messages,
      {
        author: "user",
        data: value,
      },
    ];
  };

  $: console.log("counter", counter);
</script>

<div id="bodybox">
  <div id="chatborder">
    {#each messages as message}
      <p style="text-align: {message.author === 'user' ? 'right' : 'left'}">
        {message.data}
      </p>
    {/each}
    <input
      type="text"
      name="chat"
      bind:value={userMessage}
      placeholder="Hi there! Type here to talk to me."
    />
    <button type="button" on:click={sendHandler}>Send</button>
    {#if is_buttons == 1}
      {#each buttons as button}
        <button type="button" on:click={() => questionHandler(button.name)}
          >{button.text}</button
        >
      {/each}
    {/if}
  </div>
</div>
