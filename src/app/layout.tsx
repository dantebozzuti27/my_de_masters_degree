import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { ProgressProvider } from "@/hooks/useProgress";
import { Navigation } from "@/components/Navigation";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "SDE Tracker - Senior Data Engineer Study Plan",
  description: "Track your progress through the 2-year Senior Data Engineer study plan. 416 sessions to reach $200k+.",
  icons: {
    icon: "/favicon.ico",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-gray-50 dark:bg-gray-950`}
      >
        <ProgressProvider>
          <div className="flex flex-col md:flex-row min-h-screen">
            <Navigation />
            <main className="flex-1 pb-20 md:pb-0 overflow-auto">
              {children}
            </main>
          </div>
        </ProgressProvider>
      </body>
    </html>
  );
}
