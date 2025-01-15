import React from 'react';
import styles from './Layout.module.css';

interface LayoutProps {
    children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <h1>StellarAgent</h1>
            </header>
            <nav className={styles.sidebar}>
                <ul>
                    <li>Navigation Item 1</li>
                    <li>Navigation Item 2</li>
                    <li>Navigation Item 3</li>
                </ul>
            </nav>
            <main className={styles.content}>
                {children}
            </main>
        </div>
    );
};

export default Layout;
