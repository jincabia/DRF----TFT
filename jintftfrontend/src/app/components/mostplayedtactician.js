'use client';
import { useState } from "react";
import Image from "next/image";
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import { Accordion, AccordionSummary, AccordionDetails, Typography,  Box } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

import { purple, red,blueGrey, blue, grey } from '@mui/material/colors';

// const accent = purple.A200; // #e040fb (alternative method)


export default function MostUsedTactician({ name, path, placement, gameCount }) {
  
  return (
    <Box sx={{ maxWidth: 300, p: 2, bgcolor: '#0f172a', borderRadius: 2 }}>
      {/* Header */}
      <Box display="flex" alignItems="center" justifyContent="center" mb={2} borderBottom={1} borderColor="#1f3940" padding={1}>
        <AccessTimeIcon sx={{ color: 'white', mr: 1 }} fontSize="xs" />
        <Typography variant="body2" sx={{ color: '#8a90a9', fontWeight: 'medium', textTransform: 'uppercase' }}>
          Most played Tactician
        </Typography>
      </Box>

      {/* Tactician Image */}
      <Box sx={{ display: 'flex', justifyContent: 'center' }}>
        <Image
          src={`/img/tft-tactician/${path}`}
          width={200}
          height={200}
          alt="Tactician"
          className="shadow-lg rounded-t-lg"
        />
      </Box>

      {/* Tactician Name */}

      <div>
        hi
      </div>

      <Box sx={{ bgcolor: '#1f3940', py: 1, borderRadius: 1, textAlign: 'center', width:'full' }}>
        <Typography variant="body2" sx={{ color: '#ced4f0', fontWeight: 'bold', textTransform: 'uppercase' }}>
          {name}
        </Typography>
      </Box>

      {/* Dropdown for Placement and Game Count */}
      <Accordion sx={{ mt: 2, bgcolor: 'primary.light' }}>
        <AccordionSummary expandIcon={<ExpandMoreIcon sx={{ color: 'text.secondary' }} />}>
          <Typography sx={{ color: 'text.secondary', fontWeight: 'bold', fontSize: 14 }}>Details</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography variant="body2" sx={{ mb: 1 }}>Placement: {placement}</Typography>
          <Typography variant="body2">Games Played: {gameCount}</Typography>
        </AccordionDetails>
      </Accordion>
    </Box>
  );
}
