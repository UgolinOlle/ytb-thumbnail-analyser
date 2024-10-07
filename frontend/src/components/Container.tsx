import { cn } from '~/lib/utils';

type ContainerProps = {
  className?: string;
  children: React.ReactNode;
};

export const Container: React.FC<ContainerProps> = ({ className, children }) => {
  // --- Render
  return <section className={cn('mx-auto max-w-3xl px-4 py-10 md:py-0', className)}>{children}</section>;
};
