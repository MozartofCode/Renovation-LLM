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
            className={`p-2 rounded-lg transition-colors flex items-center justify-center w-8 h-8 ${
              message.trim() && !disabled
                ? 'bg-blue-500 hover:bg-blue-600'
                : 'bg-gray-300 dark:bg-gray-600 cursor-not-allowed'
            }`}
            aria-label="Send message"
          >
            <svg
              viewBox="0 0 24 24"
              className={`w-4 h-4 transform rotate-90 transition-transform ${
                message.trim() && !disabled ? 'text-white' : 'text-gray-400'
              }`}
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M7 11L12 6L17 11M12 18V7"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
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