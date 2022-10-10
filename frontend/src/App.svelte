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
  let is_buttons: boolean = true;
  let id: string;

  let socket: WebSocket;

  onMount(() => {
    socket = new WebSocket("ws://localhost:9191/chat");
    socket.onmessage = (message) => {
      
    console.log("id", JSON.parse(message.data));
      id = JSON.parse(message.data).id;
      buttons = JSON.parse(message.data).buttons;
      is_buttons = JSON.parse(message.data).is_buttons;
      messages = [
        ...messages,
        {
          author: "bot",
          data: JSON.parse(message.data).text,
        },
      ];
    };

    socket.addEventListener("open", () => {
      console.log("Opened");
    });
  });

  const sendHandler = async () => {
    socket.send(id + ";1;" + userMessage);
    messages = [
      ...messages,
      {
        author: "user",
        data: userMessage,
      },
    ];
    userMessage = "";
  };

  const questionHandler = (value: string, text: string) => {
    // if STR
    socket.send(id + ";0;" + value);
    messages = [
      ...messages,
      {
        author: "user",
        data: text,
      },
    ];
  };

</script>

<div class = "name">
  <img class="picture" src = "Avatar.png" alt="intelligent assistent"/>
  <p class="phrase"><br>Привет! Я ???.<br>
    Виртуальный помощник.</p>
  </div>
<div id="bodybox">
  <div id="chatborder">
    {#each messages as message}
      <p class="test" style="text-align: {message.author === 'user' ? 'right' : 'left'}">
        {message.data}
      </p>
    {/each}
    <input
      class="message"
      type="text"
      name="chat"
      bind:value={userMessage}
      placeholder="Сообщение"
    />
    <button type="button" class="send" on:click={sendHandler}>Send</button>
    <p>{#if is_buttons == true}
      {#each buttons as button}
        <button type="button" class="box" on:click={() => questionHandler(button.name, button.text)}
          >{button.text}</button> &nbsp;
      {/each} 
    {/if} </p>
  </div>
</div>
