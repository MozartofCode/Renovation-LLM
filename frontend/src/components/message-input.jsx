"use client";
import React, {useRef, useState} from "react";
import FileUpload from "../components/file-upload";

function MessageInput({
  onSubmit,
  onFileSelect,
  disabled,
  placeholder = "Type a message...",
}) {
  const [message, setMessage] = useState("");
  const textareaRef = useRef(null);

  const handleTextareaChange = (e) => {
    setMessage(e.target.value);
    if (textareaRef.current) {
      textareaRef.current.style.height = "inherit";
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim() && onSubmit) {
      onSubmit(message);
      setMessage("");
      if (textareaRef.current) {
        textareaRef.current.style.height = "inherit";
      }
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 p-4"
    >
      <div className="flex items-end gap-2">
        <textarea
          ref={textareaRef}
          value={message}
          onChange={handleTextareaChange}
          placeholder={placeholder}
          disabled={disabled}
          rows={1}
          className="flex-1 resize-none bg-transparent border-0 focus:ring-0 focus:outline-none text-gray-900 dark:text-gray-100 font-inter text-sm min-h-[24px] max-h-[200px] py-0"
          name="message"
        />
        <div className="flex items-center gap-2">
          <FileUpload onFileSelect={onFileSelect} />
          <button
            type="submit"
            disabled={!message.trim() || disabled}
            className="p-2 rounded-lg bg-blue-500 hover:bg-blue-600 disabled:bg-gray-300 dark:disabled:bg-gray-600 transition-colors"
            aria-label="Send message"
          >
            <i className="fas fa-paper-plane text-white" />
          </button>
        </div>
      </div>
    </form>
  );
}

function MessageInputStory() {
  const [messages, setMessages] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);

  const handleSubmit = (message) => {
    setMessages([...messages, { text: message, type: "user" }]);
  };

  return (
    <div className="p-4 space-y-4">
      <div className="max-w-3xl mx-auto">
        {messages.map((msg, index) => (
          <div key={index} className="mb-2 text-sm font-inter">
            {msg.text}
          </div>
        ))}
        <MessageInput
          onSubmit={handleSubmit}
          onFileSelect={setSelectedFile}
          placeholder="Send a message..."
        />
        <MessageInput disabled={true} placeholder="This input is disabled" />
      </div>
    </div>
  );
}

export default MessageInput;