'use client';

import { Upload } from 'lucide-react';
import { useState } from 'react';
import { motion } from 'framer-motion';
import { cn } from '~/lib/utils';

export const Uploader: React.FC = () => {
  // --- Variables
  const [isUploading, setIsUploading] = useState(false);
  const [isHovered, setIsHovered] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const containerColor = isUploading
    ? 'text-orange-500 border-orange-500'
    : file
      ? 'text-green-500 border-green-500'
      : 'text-primary border-primary';
  const iconColor = isUploading ? 'text-orange-500' : file ? 'text-green-500' : 'text-primary';

  // --- Functions
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setIsUploading(true);
      setTimeout(() => {
        setFile(file);
        setIsUploading(false);
      }, 2000);
    }
  };

  // --- Render
  return (
    <div className="aspect-square h-[500px] w-[500px]">
      <div
        className="relative flex h-full w-full items-center justify-center overflow-hidden"
        onMouseEnter={() => !isUploading && !file && setIsHovered(true)}
        onMouseLeave={() => !isUploading && !file && setIsHovered(false)}
      >
        <motion.div
          className={cn(
            'group/uploader relative h-full w-full rounded-lg bg-white transition duration-300 ease-in-out',
            containerColor
          )}
          initial={{ border: '2px', borderStyle: 'solid' }}
          whileHover={!isUploading && !file ? { borderStyle: 'dotted' } : {}}
          transition={{ duration: 0.3, ease: 'easeInOut' }}
        >
          <div
            className={cn(
              `relative h-full w-full rounded-lg transition-all duration-300 ease-in-out`,
              isUploading
                ? 'animate-pulse shadow-[0_0_30px_rgba(255,165,0,0.8)]'
                : file
                  ? 'shadow-[0_0_30px_rgba(0,255,0,0.8)]'
                  : ''
            )}
          >
            <div className="absolute inset-0 flex flex-col items-center justify-center space-y-4 p-4">
              <label
                htmlFor="file"
                className={cn(
                  'flex cursor-pointer flex-col items-center text-center transition-all duration-300 ease-in-out',
                  containerColor,
                  !isUploading && !file && 'group-hover/uploader:text-primary'
                )}
              >
                <motion.div
                  className={cn(
                    `absolute z-10 rounded-lg opacity-20`,
                    isUploading ? 'bg-orange-500' : file ? 'bg-green-500' : 'bg-primary'
                  )}
                  style={{ width: 54, height: 54 }}
                  animate={{
                    translateX: isHovered && !isUploading && !file ? -5 : 0,
                    translateY: isHovered && !isUploading && !file ? 5 : 0,
                  }}
                  transition={{ duration: 0.3, ease: 'easeInOut' }}
                />
                <Upload
                  className={cn(
                    `z-20 h-12 w-12 transition-all duration-300 ease-in-out`,
                    iconColor,
                    `${isUploading ? 'animate-bounce' : ''}`,
                    `${!isUploading && !file && 'group-hover/uploader:-translate-y-2 group-hover/uploader:translate-x-2 group-hover/uploader:scale-110'}`,
                    `group-hover/uploader:drop-shadow-[0_0_10px_rgba(59,130,246,0.8)]`
                  )}
                />
                <span className="mt-4 text-lg font-semibold">Upload a file</span>
                <p className="mt-1 text-sm">
                  {isUploading
                    ? 'Uploading...'
                    : file
                      ? 'Upload Successful!'
                      : 'Drag and drop or click to select a PNG file'}
                </p>
              </label>
              <input type="file" id="file" className="hidden" accept=".png" onChange={handleFileChange} />
            </div>
          </div>
        </motion.div>
      </div>
    </div>
  );
};
