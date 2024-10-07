import { SizeRuleToggle } from './SizeRuleToggler';

export const Menu: React.FC = () => {
  // --- Render
  return (
    <nav className="absolute bottom-2 right-2">
      <SizeRuleToggle />
    </nav>
  );
};
