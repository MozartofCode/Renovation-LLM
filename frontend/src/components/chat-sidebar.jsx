"use client";
import React from "react";

function ChatSidebar({ chats = [], activeChat, onChatSelect, onNewChat }) {
  return (
    <div className="flex flex-col h-full bg-gray-900 text-gray-100 w-[260px] p-2">
      <button
        onClick={onNewChat}
        className="flex items-center gap-2 w-full p-3 rounded-lg border border-gray-700 hover:bg-gray-800 transition-colors mb-4"
      >
        <i className="fas fa-plus text-sm" />
        <span className="font-inter text-sm">New chat</span>
      </button>

      <div className="flex-1 overflow-y-auto">
        {chats.map((chat) => (
          <button
            key={chat.id}
            onClick={() => onChatSelect(chat.id)}
            className={`flex items-center gap-2 w-full p-3 rounded-lg hover:bg-gray-800 transition-colors mb-2 text-left ${
              activeChat === chat.id ? "bg-gray-800" : ""
            }`}
          >
            <i className="fas fa-message text-sm" />
            <span className="font-inter text-sm truncate">{chat.title}</span>
          </button>
        ))}
      </div>
    </div>
  );
}

function ChatSidebarStory() {
  const [activeChat, setActiveChat] = useState("1");
  const sampleChats = [
    { id: "1", title: "Home renovation ideas" },
    { id: "2", title: "Kitchen remodeling costs" },
    { id: "3", title: "Bathroom design inspiration" },
    { id: "4", title: "Paint color suggestions" },
    { id: "5", title: "Flooring options comparison" },
  ];

  return (
    <div className="h-[600px] w-fit">
      <ChatSidebar
        chats={sampleChats}
        activeChat={activeChat}
        onChatSelect={setActiveChat}
        onNewChat={() => console.log("New chat clicked")}
      />
    </div>
  );
}

export default ChatSidebar;