<script lang="ts">
  import { afterUpdate, onMount } from "svelte";

  // store subscriptions
  type Message = {
    author: "bot" | "user";
    data: string[];
  };
  type ButtonMsg = {
    name: string;
    text: string;
  };


  let element;
  let messages: Message[] = [];
  let userMessage: string;
  let buttons: ButtonMsg[] = [];
  let is_buttons: boolean = true;
  let id: string = "-1";

  let socket: WebSocket;

  onMount(() => {
    try {
      socket = new WebSocket("ws://localhost:9191/chat");
      socket.onmessage = (message) => {
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
    }
    catch (error) {
      console.error(error);
      messages = [
        ...messages,
        {
          author: "bot",
          data: "К сожалению, сервер сейчас недоступен. Попробуйте зайти позднее...",
        },
      ];
    }
  });

  const scrollToBottom = async (node) => {
    node.scroll({ top: node.scrollHeight, behavior: 'smooth' });
  }; 

  afterUpdate(() => {
    scrollToBottom(element);
  });

  const sendHandler = async () => {
    socket.send(id + ";1;" + userMessage);
    messages = [
      ...messages,
      {
        author: "user",
        data: [userMessage],
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
        data: [text],
      },
    ];
  };


</script>


<div class = "name">
  <img class="picture" src = "Avatar.png" alt="intelligent assistent"/>
  <p class="phrase"><br>Привет! "Я всё сам".<br>
    Виртуальный помощник.</p>
  </div>
<div id="bodybox">
  <div bind:this={element} id="chatborder">
    {#each messages as message}
    <br><p class="{message.author === 'user' ? 'message-right' : 'message-left'}">  
        {#each message.data as sent}
          {#if sent[0] == "~"}
            {#if sent[1] == "n"}
              <br>
            {/if}
            {#if sent[1] == "a"}
              {#if sent[2] == "d"}
                <a href="./files/{sent.replace('~ad', '')}" download="{decodeURI(sent.replace('~ad', ''))}" style="color: #303030">Скачать</a>
              {/if}
              {#if sent[2] == "u"}
                <a href="{sent.slice(3, sent.indexOf('~t'))}">{sent.slice(sent.indexOf('~t')+2)}</a>
              {/if}
            {/if}
          {/if}
          {#if sent[0] != "~"}
            {sent}
          {/if}
        {/each}
        </p>
        {#if message.author === 'user' }
        <br><br>
       {/if}
    {/each}

    <input
      class="message"
      type="text"
      name="chat"
      bind:value={userMessage}
      placeholder="Сообщение"
    />

    <button type="button" class="send" on:click={sendHandler}><img class = "send-p" src = "favicon.svg" alt = "Отправить"></button>
    
    <p style = "text-align: center">
      {#if is_buttons == true}
        {#each buttons as button}
          <button type="button" class="box" on:click={() => questionHandler(button.name, button.text)}>
          {button.text}</button> &nbsp;
       {/each} 
     {/if}
    </p>
  </div>
</div>
