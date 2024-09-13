import { Button, ThemeColorToggle, ThemeModeToggle } from "@/components";


export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
       <div
          className="fixed bottom-0 left-0 flex h-48 w-full items-end justify-center bg-gradient-to-t
            from-white via-white dark:from-black dark:via-black lg:static lg:size-auto
            lg:bg-none gap-x-1"
        >
          <ThemeColorToggle />
          <ThemeModeToggle />
        </div>
    </div>
  );
}
