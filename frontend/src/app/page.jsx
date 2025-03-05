"use client";
import React from "react";

function MainComponent() {
  const [chats, setChats] = useState([
    { id: "1", title: "Home renovation ideas" },
    { id: "2", title: "Kitchen remodeling costs" },
    { id: "3", title: "Bathroom design inspiration" },
  ]);

  const [activeChat, setActiveChat] = useState(null);
  const [messages, setMessages] = useState([]);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const handleNewChat = useCallback(() => {
    const newChat = {
      id: String(Date.now()),
      title: "New Chat",
    };
    setChats((prev) => [newChat, ...prev]);
    setActiveChat(newChat.id);
    setMessages([]);
  }, []);

  const handleSubmit = useCallback((message) => {
    setMessages((prev) => [
      ...prev,
      { type: "user", content: message },
      {
        type: "assistant",
        content:
          "I'm RenovateGPT, your home renovation assistant. How can I help you today?",
      },
    ]);
  }, []);

  const handleFileSelect = useCallback((file) => {
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setMessages((prev) => [
          ...prev,
          {
            type: "user",
            content: "Here's an image of my space:",
            imageUrl: e.target.result,
          },
          {
            type: "assistant",
            content:
              "I see the image of your space. What would you like to know about renovating it?",
          },
        ]);
      };
      reader.readAsDataURL(file);
    }
  }, []);

  return (
    <div className="flex h-screen bg-gray-50 dark:bg-gray-900">
      <div
        className={`fixed md:relative z-40 ${
          sidebarOpen ? "translate-x-0" : "-translate-x-full"
        } md:translate-x-0 transition-transform duration-300 ease-in-out`}
      >
        <ChatSidebar
          chats={chats}
          activeChat={activeChat}
          onChatSelect={setActiveChat}
          onNewChat={handleNewChat}
        />
      </div>

      <div className="flex flex-col flex-1 h-full overflow-hidden">
        <header className="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700">
          <button
            onClick={() => setSidebarOpen((prev) => !prev)}
            className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 md:hidden"
          >
            <i className="fas fa-bars text-gray-600 dark:text-gray-300" />
          </button>
          <h1 className="text-xl font-bold text-gray-900 dark:text-gray-100 font-inter">
            RenovateGPT
          </h1>
          <div className="w-10" />
        </header>

        <main className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.length === 0 ? (
            <div className="flex flex-col items-center justify-center h-full text-center p-8">
              <i className="fas fa-home text-4xl mb-4 text-gray-400 dark:text-gray-600" />
              <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 font-inter mb-2">
                Welcome to RenovateGPT
              </h2>
              <p className="text-gray-600 dark:text-gray-400 font-inter">
                Your AI assistant for home renovation projects. How can I help
                you today?
              </p>
            </div>
          ) : (
            messages.map((message, index) => (
              <ChatMessage
                key={index}
                type={message.type}
                content={message.content}
                imageUrl={message.imageUrl}
              />
            ))
          )}
        </main>

        <div className="p-4 border-t border-gray-200 dark:border-gray-700">
          <MessageInput
            onSubmit={handleSubmit}
            onFileSelect={handleFileSelect}
            placeholder="Ask about your renovation project..."
          />
        </div>
      </div>
    </div>
  );
}

export default MainComponent;