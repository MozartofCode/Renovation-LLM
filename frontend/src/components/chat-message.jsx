"use client";
import React from "react";

function ChatMessage({ type, content, imageUrl }) {
  const isUser = type === "user";

  return (
    <div className={`flex w-full ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-[80%] rounded-2xl p-4 ${
          isUser ? "bg-gray-100 dark:bg-gray-800" : "bg-white dark:bg-gray-900"
        }`}
      >
        <div className="font-inter text-gray-900 dark:text-gray-100 text-sm">
          {content}
        </div>
        {imageUrl && (
          <img
            src={imageUrl}
            alt={`${type} shared image`}
            className="mt-2 rounded-lg max-w-full h-auto"
          />
        )}
      </div>
    </div>
  );
}

function ChatMessageStory() {
  return (
    <div className="space-y-4 p-4 bg-gray-50 dark:bg-gray-950">
      <ChatMessage
        type="user"
        content="Here's a photo from my recent trip!"
        imageUrl="https://images.pexels.com/photos/2662116/pexels-photo-2662116.jpeg"
      />

      <ChatMessage
        type="assistant"
        content="That's a beautiful landscape! The mountains look majestic."
      />

      <ChatMessage type="user" content="Thanks! It was taken during sunrise." />

      <ChatMessage
        type="assistant"
        content="Here's an AI generated visualization of a similar scene."
        imageUrl="https://images.pexels.com/photos/1261728/pexels-photo-1261728.jpeg"
      />
    </div>
  );
}

export default ChatMessage;