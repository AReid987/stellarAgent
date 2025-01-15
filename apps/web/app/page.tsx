import styles from "./page.module.css";
import Layout from '../components/Layout';

export default function Home() {
  return (
    <Layout>
      <div className={styles.page}>
        <main className={styles.main}>
        </main>
        <footer className={styles.footer}>
          <a
            href="https://vercel.com/templates?search=turborepo&utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
          >
            Examples
          </a>
          <a
            href="https://turbo.build?utm_source=create-turbo"
            target="_blank"
            rel="noopener noreferrer"
          >
            Go to turbo.build →
          </a>
        </footer>
      </div>
    </Layout>
  );
}
