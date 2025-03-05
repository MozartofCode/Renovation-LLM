"use client";
import React from "react";

function FileUpload({ onFileSelect }) {
  const fileInputRef = React.useRef(null);

  const handleClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files?.[0];
    if (file && onFileSelect) {
      onFileSelect(file);
    }
  };

  return (
    <div className="inline-block">
      <button
        onClick={handleClick}
        className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
        aria-label="Upload image"
        type="button"
      >
        <i className="fas fa-camera text-gray-600 dark:text-gray-300" />
      </button>
      <input
        ref={fileInputRef}
        type="file"
        accept="image/*"
        onChange={handleFileChange}
        className="hidden"
        name="file-upload"
      />
    </div>
  );
}

function FileUploadStory() {
  const [selectedFile, setSelectedFile] = React.useState(null);

  return (
    <div className="p-4 space-y-4">
      <div className="flex items-center gap-4">
        <FileUpload onFileSelect={setSelectedFile} />
        <span className="text-sm text-gray-600 dark:text-gray-300">
          {selectedFile ? `Selected: ${selectedFile.name}` : "No file selected"}
        </span>
      </div>
    </div>
  );
}

export default FileUpload;