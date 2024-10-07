import { Container } from '~/components/Container';
import { Header } from '~/components/Header';
import { Uploader } from '~/components/Uploader';
import { Grid } from '~/components/Grid';

import '~/styles/App.css';

export default function App() {
  // --- Render
  return (
    <Container className="flex min-h-screen w-full flex-col items-center justify-center gap-10 md:gap-20">
      <Grid />
      <Header className="text-primary" align="center">
        Youtube Thumbnails Analyser
      </Header>
      <Uploader />
    </Container>
  );
}
