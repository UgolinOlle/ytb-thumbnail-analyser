'use client';

import React, { useState, useEffect } from 'react';

interface GridProps {
  className?: string;
}

export const Grid: React.FC<GridProps> = ({ className = '' }) => {
  // --- Variables
  const [gridSize, setGridSize] = useState(20);
  const [blueSquares, setBlueSquares] = useState<Set<number>>(new Set());

  // --- Functions
  useEffect(() => {
    const updateGridSize = () => {
      const size = Math.floor(Math.min(window.innerWidth, window.innerHeight) / 50);
      setGridSize(size);
    };

    updateGridSize();
    window.addEventListener('resize', updateGridSize);
    return () => window.removeEventListener('resize', updateGridSize);
  }, []);

  useEffect(() => {
    const generateBlueSquares = () => {
      const totalSquares = gridSize * gridSize;
      const newBlueSquares = new Set<number>();
      const numberOfBlueSquares = Math.floor(totalSquares * 0.03);

      while (newBlueSquares.size < numberOfBlueSquares) {
        newBlueSquares.add(Math.floor(Math.random() * totalSquares));
      }

      setBlueSquares(newBlueSquares);
    };

    generateBlueSquares();
    const interval = setInterval(generateBlueSquares, 2000);

    return () => clearInterval(interval);
  }, [gridSize]);

  // --- Render
  return (
    <div className={`fixed inset-0 -z-10 ${className}`}>
      <div
        className="grid h-full w-full"
        style={{
          gridTemplateColumns: `repeat(${gridSize}, minmax(0, 1fr))`,
          gridTemplateRows: `repeat(${gridSize}, minmax(0, 1fr))`,
        }}
      >
        {[...Array(gridSize * gridSize)].map((_, i) => (
          <div
            key={i}
            className={`border-b border-r border-primary/10 last:border-r-0 [&:nth-child(${gridSize}n)]:border-r-0 transition-colors duration-300 ${blueSquares.has(i) ? 'bg-primary/50' : ''}`}
          />
        ))}
      </div>
    </div>
  );
};
