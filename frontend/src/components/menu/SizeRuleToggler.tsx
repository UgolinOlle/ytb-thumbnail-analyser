'use client';

import { useEffect, useState } from 'react';
import { Grid2x2Check, Grid2x2X } from 'lucide-react';

import { Button } from '~/components/ui/button';

export const SizeRuleToggle: React.FC = () => {
  const [sizeRule, setSizeRule] = useState<boolean>(() => {
    const storedValue = localStorage.getItem('size-rule');
    return storedValue === 'true';
  });

  useEffect(() => {
    localStorage.setItem('size-rule', sizeRule.toString());
  }, [sizeRule]);

  const toggleSizeRule = () => {
    setSizeRule((prev) => !prev);
  };

  return (
    <Button onClick={toggleSizeRule} className="rounded-full py-4">
      {sizeRule ? <Grid2x2X /> : <Grid2x2Check />}
    </Button>
  );
};
