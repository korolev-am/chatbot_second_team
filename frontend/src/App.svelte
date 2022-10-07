<script lang="ts">
  import { onMount } from "svelte";

  // store subscriptions
  type Message = {
    author: "bot" | "user";
    data: string;
  };
  type Buttons = {
    [key: number]: string[];
  };

  let messages: Message[] = [];
  let userMessage: string;
  let buttons: Buttons = {
    1: ["Блок 1, вопрос 1", "Блок 1, вопрос 2", "Блок 1, вопрос 3"],
    2: ["Блок 2, вопрос 1", "Блок 2, вопрос 2"],
    3: [
      "Блок 3, вопрос 1",
      "Блок 3, вопрос 2",
      "Блок 3, вопрос 3",
      "Блок 3, вопрос 4",
    ],
    4: [],
  };
  let counter: number = 1;

  let socket: WebSocket;

  onMount(() => {
    socket = new WebSocket("ws://localhost:9191/chat");
    socket.onmessage = (message) => {
      messages = [
        ...messages,
        {
          author: "bot",
          data: message.data,
        },
      ];
    };
    socket.addEventListener("open", () => {
      console.log("Opened");
    });
  });

  const sendHandler = async () => {
    socket.send(userMessage);
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
    socket.send(value);
    messages = [
      ...messages,
      {
        author: "user",
        data: value,
      },
    ];
    if (counter < 4) counter += 1;
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
    <!-- <input
      type="text"
      name="chat"
      bind:value={userMessage}
      placeholder="Hi there! Type here to talk to me."
    /> -->
    <!-- <button type="button" on:click={sendHandler}>Send</button> -->
    {#each buttons[counter] as buttonText}
      <button type="button" on:click={() => questionHandler(buttonText)}
        >{buttonText}</button
      >
    {/each}
  </div>
</div>
