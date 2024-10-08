import { SizeRuleToggle } from './SizeRuleToggler';

export const Menu: React.FC = () => {
  // --- Render
  return (
    <nav className="fixed bottom-2 right-2">
      <SizeRuleToggle />
    </nav>
  );
};
