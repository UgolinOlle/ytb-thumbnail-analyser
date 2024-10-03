type ContainerProps = {
  children: React.ReactNode;
};

export const Container: React.FC<ContainerProps> = ({ children }) => {
  // --- Render
  return <section className="max-w-3xl mx-auto px-4">{children}</section>;
};
