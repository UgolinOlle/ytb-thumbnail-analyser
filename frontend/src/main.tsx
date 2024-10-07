import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { Toaster } from 'sonner';

import '~/styles/index.css';

import App from './App.tsx';
import { Menu } from '~/components/menu/Menu.tsx';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
    <Toaster richColors position="top-center" />
    <Menu />
  </StrictMode>
);
