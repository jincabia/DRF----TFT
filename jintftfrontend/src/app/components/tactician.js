import { Box, Typography, Paper } from '@mui/material';
import Image from 'next/image';

export default function TacticianDisplay({ tacticianPath, tacticianAvgPlacement }) {
  return (
    <>
      {tacticianPath ? (
        <Paper
          sx={{
            maxWidth: '300px',
            padding: 4,
            borderRadius: 2,
            backgroundColor: 'primary.dark',
            textAlign: 'center',
          }}
          elevation={6}
        >
          <Typography variant="h5" component="h1" gutterBottom>
            Most played Tactician
          </Typography>

          <Image
            src={`/img/tft-tactician/${tacticianPath}`}
            width={200}
            height={200}
            alt="Picture of Tactician"
            style={{ borderRadius: '8px', boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.5)' }}
          />

          <Typography variant="h6" component="p" mt={2}>
            Average Placement: {tacticianAvgPlacement}
          </Typography>
        </Paper>
      ) : (
        <Box>
          <Typography variant="body1" color="error">
            No path found
          </Typography>
        </Box>
      )}
    </>
  );
}
