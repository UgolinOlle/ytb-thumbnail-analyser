import { cva, VariantProps } from "class-variance-authority";

import { cn } from "~/lib/utils";

// -- Header Variants
const headerVariants = cva(
  "text-lg font-semibold text-neutral-900 dark:text-neutral-200",
  {
    variants: {
      variant: {
        hero: "lg:text-8xl md:text-7xl text-6xl font-light",
        h1: "lg:text-5xl md:text-4xl text-3xl font-bold",
        h2: "lg:text-3xl md:text-2xl text-xl font-bold",
        h3: "lg:text-2xl md:text-xl text-lg font-bold",
        h4: "lg:text-xl md:text-lg text-base font-bold",
      },
      align: {
        left: "justify-start leading-snug md:leading-normal text-center md:text-left",
        center: "justify-center leading-snug md:leading-normal text-center",
        right:
          "justify-end text-center leading-snug md:leading-normal md:text-right",
      },
    },
    defaultVariants: {
      variant: "h1",
      align: "left",
    },
  },
);

export interface IHeaderProps
  extends React.HTMLAttributes<HTMLHeadingElement>,
    VariantProps<typeof headerVariants> {
}

/**
 * @name Header
 * @description A header component that can be used to display different heading sizes.
 * @exports Header
 */
export const Header: React.FC<IHeaderProps> = ({
  variant,
  align,
  className,
  ...props
}) => {
  // --- Render
  return (
    <div
      className={cn(
        "flex w-full items-center",
        headerVariants({ align }),
      )}
    >
      <h1 className={cn(headerVariants({ variant }), className)}>
        {props.children}
      </h1>
    </div>
  );
};
