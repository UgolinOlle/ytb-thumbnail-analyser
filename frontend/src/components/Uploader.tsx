'use client';

import { Upload, X } from 'lucide-react';
import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { cn } from '~/lib/utils';
import axios from 'axios';
import { z } from 'zod';
import { toast } from 'sonner';

const fileSchema = z.object({
  file: z.instanceof(File).refine((file) => file.type === 'image/png', {
    message: 'Seules les images PNG sont acceptées.',
  }),
});

interface AnalysisResult {
  comment: string;
  score: number;
  imageUrl: string;
}

export const Uploader: React.FC = () => {
  // --- Variables
  const [isUploading, setIsUploading] = useState(false);
  const [isHovered, setIsHovered] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);
  const [containerWidth, setContainerWidth] = useState(0);
  const containerRef = useRef<HTMLDivElement>(null);

  const containerColor = isUploading
    ? 'text-orange-500 border-orange-500'
    : file
      ? 'text-green-500 border-green-500'
      : 'text-primary border-primary';

  const iconColor = isUploading ? 'text-orange-500' : file ? 'text-green-500' : 'text-primary';

  useEffect(() => {
    const updateWidth = () => {
      if (containerRef.current) {
        setContainerWidth(containerRef.current.offsetWidth);
      }
    };

    updateWidth();
    window.addEventListener('resize', updateWidth);
    return () => window.removeEventListener('resize', updateWidth);
  }, []);

  // --- Functions
  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    setFile(selectedFile || null);

    if (selectedFile) {
      try {
        const validatedFile = fileSchema.parse({ file: selectedFile });

        setIsUploading(true);

        const formData = new FormData();
        formData.append('file', validatedFile.file);

        const response = await axios.post('http://127.0.0.1:8000/api/v1/thumbnail/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        toast.success('Analyse réussie !');
        setAnalysisResult({
          comment: response.data.comment,
          score: response.data.score,
          imageUrl: URL.createObjectURL(selectedFile),
        });
      } catch (error) {
        if (error instanceof z.ZodError) toast.error(error.errors[0]?.message || 'Erreur de validation');
        else toast.error("Erreur lors de l'analyse de la miniature");
      } finally {
        setIsUploading(false);
      }
    }
  };

  const resetUploader = () => {
    setFile(null);
    setAnalysisResult(null);
  };

  const getScoreColor = (score: number) => {
    if (score < 4) return 'bg-red-500';
    if (score < 6) return 'bg-orange-500';
    return 'bg-green-500';
  };

  // --- Render
  return (
    <div className="w-full" ref={containerRef}>
      <AnimatePresence initial={false} mode="wait">
        {!analysisResult ? (
          <motion.div
            key="uploader"
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: 50 }}
            transition={{ duration: 0.3 }}
            className="relative w-full"
            style={{ height: containerWidth }}
            onMouseEnter={() => !isUploading && !file && setIsHovered(true)}
            onMouseLeave={() => !isUploading && !file && setIsHovered(false)}
          >
            <motion.div
              className={cn(
                'group/uploader absolute inset-0 flex items-center justify-center rounded-lg bg-white transition duration-300 ease-in-out',
                containerColor
              )}
              initial={{ border: '2px', borderStyle: 'solid' }}
              whileHover={!isUploading && !file ? { borderStyle: 'dotted' } : {}}
              transition={{ duration: 0.3, ease: 'easeInOut' }}
            >
              <div
                className={cn(
                  `relative flex h-full w-full items-center justify-center rounded-lg transition-all duration-300 ease-in-out`,
                  isUploading
                    ? 'animate-pulse shadow-[0_0_30px_rgba(255,165,0,0.8)]'
                    : file
                      ? 'shadow-[0_0_30px_rgba(0,255,0,0.8)]'
                      : ''
                )}
              >
                <div className="flex flex-col items-center justify-center space-y-4 p-4 text-center">
                  <label
                    htmlFor="file"
                    className={cn(
                      'flex cursor-pointer flex-col items-center transition-all duration-300 ease-in-out',
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
          </motion.div>
        ) : (
          <motion.div
            key="result"
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -50 }}
            transition={{ duration: 0.3 }}
            className="relative w-full rounded-lg bg-white shadow-lg"
            style={{ minHeight: containerWidth }}
          >
            <div className={cn('h-2 w-full rounded-t-lg', getScoreColor(analysisResult.score))} />
            <div className="absolute right-2 top-4">
              <button
                onClick={resetUploader}
                className="rounded-full bg-gray-200 p-2 text-gray-600 hover:bg-gray-300 hover:text-gray-800"
              >
                <X size={20} />
              </button>
            </div>
            <div className="flex flex-col p-6">
              <h2 className="mb-4 text-2xl font-bold text-gray-800">Analysis Result</h2>
              <div className="mb-4 flex-1 overflow-hidden">
                <img
                  src={analysisResult.imageUrl}
                  alt="Uploaded thumbnail"
                  className="mb-4 h-48 w-full rounded-xl object-cover"
                />
                <p className="mb-2 text-lg font-semibold text-gray-700">Comment:</p>
                <div className="max-h-[280px] overflow-y-auto pr-2">
                  <p className="text-gray-600">{analysisResult.comment}</p>
                </div>
              </div>
              <p className="text-lg font-semibold text-gray-700">
                Score: <span className="text-blue-600">{analysisResult.score}</span>
              </p>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};
